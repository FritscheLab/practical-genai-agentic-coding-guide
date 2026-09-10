// Let keyboard users scroll wide tables without adding tab stops to tables that fit.
(() => {
  const labMenu = document.querySelector('.guide-lab-menu');
  if (labMenu) {
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && labMenu.open) {
        labMenu.open = false;
        labMenu.querySelector('summary').focus();
      }
    });
    document.addEventListener('click', event => {
      if (!labMenu.contains(event.target)) labMenu.open = false;
    });
    labMenu.addEventListener('focusout', event => {
      if (event.relatedTarget && !labMenu.contains(event.relatedTarget)) labMenu.open = false;
    });
  }

  const wrappers = [...document.querySelectorAll('.main-content .table-wrapper')];
  const headings = [...document.querySelectorAll('.main-content h1, .main-content h2, .main-content h3')];

  wrappers.forEach((wrapper, index) => {
    const table = wrapper.querySelector('table');
    if (!table) return;

    const heading = headings.filter(element =>
      element.compareDocumentPosition(wrapper) & Node.DOCUMENT_POSITION_FOLLOWING
    ).pop();
    const title = (table.querySelector('caption')?.textContent || heading?.textContent || `Table ${index + 1}`)
      .replace(/\s+/g, ' ').trim();

    const update = () => {
      if (wrapper.scrollWidth > wrapper.clientWidth + 1) {
        wrapper.tabIndex = 0;
        wrapper.setAttribute('role', 'region');
        wrapper.setAttribute('aria-label', `${title} (scroll horizontally)`);
      } else {
        wrapper.removeAttribute('tabindex');
        wrapper.removeAttribute('role');
        wrapper.removeAttribute('aria-label');
      }
    };

    update();
    if ('ResizeObserver' in window) {
      const observer = new ResizeObserver(update);
      observer.observe(wrapper);
      observer.observe(table);
    } else {
      window.addEventListener('resize', update);
    }
  });
})();
