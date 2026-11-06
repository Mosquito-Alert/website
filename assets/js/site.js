// Lightweight site-wide interactions for navigation and language switchers.
(function () {
  const onReady = (callback) => {
    if (document.readyState !== "loading") {
      callback();
    } else {
      document.addEventListener("DOMContentLoaded", callback);
    }
  };

  onReady(() => {
    const collapseAllSubnavs = () => {
      document
        .querySelectorAll("[data-nav-item][data-subnav-open='true']")
        .forEach((item) => {
          item.dataset.subnavOpen = "false";
          const toggle = item.querySelector("[data-subnav-toggle]");
          if (toggle) {
            toggle.setAttribute("aria-expanded", "false");
          }
        });
    };

    const navToggle = document.querySelector("[data-nav-toggle]");
    const navPanel = document.querySelector("[data-header-nav]");

    if (navToggle && navPanel) {
      const closeNav = () => {
        navToggle.setAttribute("aria-expanded", "false");
        navPanel.dataset.navOpen = "false";
        collapseAllSubnavs();
      };

      const toggleNav = () => {
        const isOpen = navToggle.getAttribute("aria-expanded") === "true";
        if (isOpen) {
          closeNav();
        } else {
          navToggle.setAttribute("aria-expanded", "true");
          navPanel.dataset.navOpen = "true";
        }
      };

      navToggle.addEventListener("click", (event) => {
        event.preventDefault();
        toggleNav();
      });

      document.addEventListener("keyup", (event) => {
        if (event.key === "Escape") {
          closeNav();
        }
      });

      document.addEventListener("click", (event) => {
        if (navPanel.dataset.navOpen !== "true") {
          return;
        }

        const target = event.target;
        const clickedToggle = navToggle === target || navToggle.contains(target);
        const clickedPanel = navPanel === target || navPanel.contains(target);

        if (!clickedToggle && !clickedPanel) {
          closeNav();
        }
      });

      navPanel.addEventListener("click", (event) => {
        if (navPanel.dataset.navOpen !== "true") {
          return;
        }

        const target = event.target;
        if (target instanceof HTMLElement && target.tagName.toLowerCase() === "a") {
          closeNav();
        }
      });
    }

    document.querySelectorAll("[data-subnav-toggle]").forEach((button) => {
      const navItem = button.closest("[data-nav-item]");
      if (!navItem) {
        return;
      }

      const openSubnav = () => {
        collapseAllSubnavs();
        navItem.dataset.subnavOpen = "true";
        button.setAttribute("aria-expanded", "true");
      };

      const closeSubnav = () => {
        navItem.dataset.subnavOpen = "false";
        button.setAttribute("aria-expanded", "false");
      };

      button.addEventListener("click", (event) => {
        event.preventDefault();
        const isOpen = navItem.dataset.subnavOpen === "true";
        if (isOpen) {
          closeSubnav();
        } else {
          openSubnav();
        }
      });
    });

    document.querySelectorAll("[data-language-menu]").forEach((button) => {
      const container = button.closest(".header-top__languages");
      if (!container) {
        return;
      }

      const closeMenu = () => {
        container.dataset.open = "false";
        button.setAttribute("aria-expanded", "false");
      };

      button.setAttribute("aria-haspopup", "true");
      button.setAttribute("aria-expanded", "false");

      button.addEventListener("click", (event) => {
        event.preventDefault();
        const isOpen = container.dataset.open === "true";
        if (isOpen) {
          closeMenu();
        } else {
          container.dataset.open = "true";
          button.setAttribute("aria-expanded", "true");
        }
      });

      document.addEventListener("click", (event) => {
        if (!container.contains(event.target)) {
          closeMenu();
        }
      });

      document.addEventListener("keyup", (event) => {
        if (event.key === "Escape") {
          closeMenu();
          button.blur();
        }
      });
    });
  });
})();
