document.addEventListener('DOMContentLoaded', function() {
  const filterForm = document.getElementById('filterForm');
  filterForm.addEventListener('submit', function(e) {
    e.preventDefault();
    // You can implement your filter logic here
    // Example: collect values
    const filter = {    
      datum: document.getElementById('filterDatum').value,
      abteilung: document.getElementById('filterAbteilung').value,
      klasse: document.getElementById('filterKlasse').value
    };
    // For now, just log the filter
    console.log(filter);
  });

  const filterBtn = document.getElementById('filterBtn');
  const filterDropdown = document.getElementById('filterDropdown');

  function positionDropdown() {
    const rect = filterBtn.getBoundingClientRect();
    const dropdownWidth = 250;
    const padding = 12;

    if (window.innerWidth < 400) {
      filterDropdown.style.width = `calc(100vw - ${padding * 2}px)`;
      filterDropdown.style.left = padding + 'px';
    } else {
      let left = rect.left;
      if (left + dropdownWidth > window.innerWidth - padding) {
        left = window.innerWidth - dropdownWidth - padding;
        if (left < padding) left = padding;
      }
      if (left < padding) left = padding;
      filterDropdown.style.width = dropdownWidth + 'px';
      filterDropdown.style.left = left + 'px';
    }

    filterDropdown.style.position = 'absolute';
    filterDropdown.style.top = (rect.bottom + window.scrollY) + 'px';
    filterDropdown.style.display = 'block';
    filterDropdown.style.zIndex = 1050;
  }

  filterBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    if (filterDropdown.style.display === 'block') {
      filterDropdown.style.display = 'none';
      window.removeEventListener('resize', positionDropdown);
      window.removeEventListener('scroll', positionDropdown);
    } else {
      positionDropdown();
      window.addEventListener('resize', positionDropdown);
      window.addEventListener('scroll', positionDropdown);
    }
  });

  document.addEventListener('click', function(e) {
    if (!filterDropdown.contains(e.target) && e.target !== filterBtn) {
      filterDropdown.style.display = 'none';
      window.removeEventListener('resize', positionDropdown);
      window.removeEventListener('scroll', positionDropdown);
    }
  });

  document.getElementById('applyFilterBtn').addEventListener('click', function() {
    filterDropdown.style.display = 'none';
    window.removeEventListener('resize', positionDropdown);
    window.removeEventListener('scroll', positionDropdown);
  });
});