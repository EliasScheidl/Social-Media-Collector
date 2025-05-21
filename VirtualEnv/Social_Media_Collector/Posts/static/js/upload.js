function triggerFileInput() {
  document.getElementById('fileInput').click();
}
document.addEventListener('DOMContentLoaded', function() {
          const departmentSelect = document.getElementById('department');
          const classSelect = document.getElementById('class');
          const classOptions = {
            IT: ["1AHIT", "2AHIT", "3AHIT", "4AHIT", "5AHIT"],
            WING: [
              "1AHWIM", "2AHWIM", "3AHWIM", "4AHWIM", "5AHWIM",
              "1BHWIM", "2BHWIM", "3BHWIM", "4BHWIM", "5BHWIM"
            ],
            MBA: [
              "1AHMBA", "2AHMBA", "3AHMBA", "4AHMBA", "5AHMBA",
              "1BHMBA", "2BHMBA", "3BHMBA", "4BHMBA", "5BHMBA"
            ],
            ETEC: [
              "1AHET", "2AHET", "3AHET", "4AHET", "5AHET"
            ],
            FME: [
              "1AFME", "2AFME", "3AFME", "4AFME", "5AFME"
            ]
          };
            // Populate initial class options if a department is already selected
            if (departmentSelect.value && classOptions[departmentSelect.value]) {
            classOptions[departmentSelect.value].forEach(cls => {
              const option = document.createElement('option');
              option.value = cls;
              option.textContent = cls;
              classSelect.appendChild(option);
            });
            }

          // Clear previous options and add default option
          classSelect.innerHTML = '<option value="" disabled selected>Bitte wählen...</option>';

          // Populate initial class options if a department is already selected
          if (departmentSelect.value && classOptions[departmentSelect.value]) {
            classOptions[departmentSelect.value].forEach(cls => {
              const option = document.createElement('option');
              option.value = cls;
              option.textContent = cls;
              classSelect.appendChild(option);
            });
          }

          departmentSelect.addEventListener('change', function() {
            // Clear previous options
            classSelect.innerHTML = '<option value="" disabled selected>Bitte wählen...</option>';

            const selectedDept = departmentSelect.value;
            if (classOptions[selectedDept]) {
            classOptions[selectedDept].forEach(cls => {
              const option = document.createElement('option');
              option.value = cls;
              option.textContent = cls;
              classSelect.appendChild(option);
            });
            }
          });
          });
