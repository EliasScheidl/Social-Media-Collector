// Beispielhafte Aktionen (hier kannst du später API-Aufrufe etc. einbauen)
    document.querySelectorAll('.action-bar button').forEach(btn => {
      btn.addEventListener('click', () => {
        alert(`${btn.title} gedrückt`);
      });
    });