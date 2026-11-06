const fightSection = document.querySelector('.home-fight');

if (fightSection) {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let isActive = false;
  let ticking = false;
  let sectionOffsetTop = 0;

  const refreshSectionOffset = () => {
    sectionOffsetTop = fightSection.getBoundingClientRect().top + (window.scrollY || window.pageYOffset);
  };

  const updateOffsets = () => {
    if (!isActive) {
      ticking = false;
      return;
    }

    ticking = false;
    const scrollTop = window.scrollY || window.pageYOffset;
    const backgroundOffset = (scrollTop - sectionOffsetTop) * 0.35;
    fightSection.style.setProperty('--fight-parallax-offset', `${backgroundOffset}px`);

  };

  const requestTick = () => {
    if (!ticking) {
      window.requestAnimationFrame(updateOffsets);
      ticking = true;
    }
  };

  const handleScroll = () => {
    requestTick();
  };

  const activate = () => {
    if (isActive) {
      return;
    }

    isActive = true;
    refreshSectionOffset();
    fightSection.dataset.parallaxActive = 'true';
    requestTick();
    window.addEventListener('scroll', handleScroll, { passive: true });
  };

  const deactivate = () => {
    if (!isActive) {
      return;
    }

    isActive = false;
    ticking = false;
    fightSection.dataset.parallaxActive = 'false';
    fightSection.style.removeProperty('--fight-parallax-offset');

    window.removeEventListener('scroll', handleScroll);
  };

  const shouldActivate = () => !prefersReducedMotion.matches && window.innerWidth > 960;

  const evaluate = () => {
    if (shouldActivate()) {
      activate();
    } else {
      deactivate();
    }
  };

  const handleResize = () => {
    if (isActive) {
      refreshSectionOffset();
      requestTick();
    }

    evaluate();
  };

  window.addEventListener('resize', handleResize);

  const handleMotionChange = () => {
    evaluate();
  };

  if (typeof prefersReducedMotion.addEventListener === 'function') {
    prefersReducedMotion.addEventListener('change', handleMotionChange);
  } else if (typeof prefersReducedMotion.addListener === 'function') {
    prefersReducedMotion.addListener(handleMotionChange);
  }

  evaluate();
}
