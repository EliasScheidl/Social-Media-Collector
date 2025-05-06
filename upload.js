document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const uploadForm = document.getElementById('uploadForm');
    const uploadArea = document.getElementById('uploadArea');
    const uploadPlaceholder = document.getElementById('uploadPlaceholder');
    const uploadPreview = document.getElementById('uploadPreview');
    const fileInput = document.getElementById('fileInput');
    const submitBtn = document.getElementById('submitBtn');
    const progressBar = document.getElementById('progressBar');
    const closeBtn = document.getElementById('closeBtn');
    
    // Variables
    let selectedFiles = [];
    
    // Initialize
    function init() {
      // Event listeners
      uploadArea.addEventListener('click', triggerFileInput);
      uploadArea.addEventListener('dragover', handleDragOver);
      uploadArea.addEventListener('dragleave', handleDragLeave);
      uploadArea.addEventListener('drop', handleDrop);
      fileInput.addEventListener('change', handleFileSelect);
      uploadForm.addEventListener('input', validateForm);
      closeBtn.addEventListener('click', confirmClose);
      uploadForm.addEventListener('submit', handleSubmit);
      
      // Disable form submission on enter
      uploadForm.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          e.preventDefault();
        }
      });
    }
    
    // Trigger file input click
    function triggerFileInput() {
      fileInput.click();
    }
    
    // Handle drag over
    function handleDragOver(e) {
      e.preventDefault();
      e.stopPropagation();
      uploadArea.classList.add('drag-over');
    }
    
    // Handle drag leave
    function handleDragLeave(e) {
      e.preventDefault();
      e.stopPropagation();
      uploadArea.classList.remove('drag-over');
    }
    
    // Handle drop
    function handleDrop(e) {
      e.preventDefault();
      e.stopPropagation();
      uploadArea.classList.remove('drag-over');
      
      if (e.dataTransfer.files.length > 0) {
        const files = Array.from(e.dataTransfer.files);
        processFiles(files);
      }
    }
    
    // Handle file selection
    function handleFileSelect(e) {
      if (fileInput.files.length > 0) {
        const files = Array.from(fileInput.files);
        processFiles(files);
      }
    }
    
    // Process selected files
    function processFiles(files) {
      // Filter only images
      const imageFiles = files.filter(file => file.type.startsWith('image/'));
      
      if (imageFiles.length === 0) {
        showNotification('Bitte wählen Sie Bilder aus.', 'warning');
        return;
      }
      
      // Add files to selected files array
      selectedFiles = [...selectedFiles, ...imageFiles];
      
      // Update UI
      updateFilePreview();
      validateForm();
      
      // Simulate upload progress
      simulateUploadProgress();
    }
    
    // Update file preview
    function updateFilePreview() {
      if (selectedFiles.length > 0) {
        uploadPlaceholder.style.display = 'none';
        uploadPreview.style.display = 'flex';
        uploadPreview.innerHTML = '';
        
        selectedFiles.forEach((file, index) => {
          const reader = new FileReader();
          
          reader.onload = function(e) {
            const previewItem = document.createElement('div');
            previewItem.className = 'preview-item';
            previewItem.innerHTML = `
              <img src="${e.target.result}" alt="Preview">
              <button class="preview-remove" data-index="${index}">
                <i class="bi bi-x"></i>
              </button>
            `;
            
            uploadPreview.appendChild(previewItem);
            
            // Add event listener to remove button
            previewItem.querySelector('.preview-remove').addEventListener('click', function(e) {
              e.stopPropagation();
              removeFile(index);
            });
          };
          
          reader.readAsDataURL(file);
        });
      } else {
        uploadPlaceholder.style.display = 'block';
        uploadPreview.style.display = 'none';
        uploadPreview.innerHTML = '';
      }
    }
    
    // Remove file
    function removeFile(index) {
      selectedFiles.splice(index, 1);
      updateFilePreview();
      validateForm();
    }
    
    // Validate form
    function validateForm() {
      const abteilung = document.getElementById('abteilung').value;
      const classValue = document.getElementById('class').value;
      
      // Enable submit button if files are selected and required fields are filled
      if (selectedFiles.length > 0 && abteilung && classValue) {
        submitBtn.disabled = false;
      } else {
        submitBtn.disabled = true;
      }
    }
    
    // Simulate upload progress
    function simulateUploadProgress() {
      let width = 0;
      progressBar.style.width = '0%';
      
      const interval = setInterval(() => {
        if (width >= 100) {
          clearInterval(interval);
        } else {
          width += 5;
          progressBar.style.width = width + '%';
        }
      }, 100);
      
      // Reset after completion
      setTimeout(() => {
        progressBar.style.width = '0%';
      }, 3000);
    }
    
    // Show notification
    function showNotification(message, type) {
      // Create notification element
      const notification = document.createElement('div');
      notification.className = `notification ${type}`;
      notification.textContent = message;
      
      // Add to document
      document.body.appendChild(notification);
      
      // Remove after a delay
      setTimeout(() => {
        notification.remove();
      }, 3000);
    }
    
    // Confirm close
    function confirmClose() {
      if (selectedFiles.length > 0 || document.getElementById('beschreibung').value) {
        if (confirm('Möchten Sie den Vorgang wirklich abbrechen? Alle eingegebenen Daten gehen verloren.')) {
          window.location.href = 'index.html';
        }
      } else {
        window.location.href = 'index.html';
      }
    }
    
    // Handle form submission
    function handleSubmit(e) {
      e.preventDefault();
      
      // Get form data
      const abteilung = document.getElementById('abteilung').value;
      const classValue = document.getElementById('class').value;
      const beschreibung = document.getElementById('beschreibung').value;
      
      // Create FormData
      const formData = new FormData();
      formData.append('abteilung', abteilung);
      formData.append('class', classValue);
      formData.append('beschreibung', beschreibung);
      
      // Append files
      selectedFiles.forEach((file, index) => {
        formData.append(`file-${index}`, file);
      });
      
      // Simulate API call
      console.log('Sending data to server:', {
        abteilung,
        class: classValue,
        beschreibung,
        files: selectedFiles.map(file => file.name)
      });
      
      // Show full progress bar
      progressBar.style.width = '100%';
      
      // Simulate successful upload
      setTimeout(() => {
        showNotification('Upload erfolgreich!', 'success');
        
        // Redirect or reset form
        setTimeout(() => {
          // For demo purposes, just reset the form
          uploadForm.reset();
          selectedFiles = [];
          updateFilePreview();
          validateForm();
          progressBar.style.width = '0%';
        }, 1000);
      }, 2000);
    }
    
    // Initialize
    init();
    
    // Add CSS styles for notifications
    const style = document.createElement('style');
    style.textContent = `
      .notification {
        position: fixed;
        top: 16px;
        left: 50%;
        transform: translateX(-50%);
        padding: 12px 24px;
        border-radius: 8px;
        color: white;
        z-index: 1050;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        animation: slideDown 0.3s ease-out forwards;
      }
      
      .notification.success {
        background-color: #28a745;
      }
      
      .notification.warning {
        background-color: #ffc107;
        color: #212529;
      }
      
      .notification.error {
        background-color: #dc3545;
      }
      
      @keyframes slideDown {
        from { transform: translate(-50%, -20px); opacity: 0; }
        to { transform: translate(-50%, 0); opacity: 1; }
      }
    `;
    document.head.appendChild(style);
  });