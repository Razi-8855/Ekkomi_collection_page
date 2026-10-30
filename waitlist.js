/**
 * EKKOMI NOCTURNE — JOIN THE WAITING LIST CONTROLLER
 * Multi-step, editorial, high-fashion modal experience.
 *
 * Prepared for:
 * 1. Local & Remote backend registration storage
 * 2. Real email confirmation delivery (SendGrid / Postmark / SES / Shopify Email)
 * 3. Shopify inventory verification & native Add to Cart / Buy Now integration
 */

(function () {
  'use strict';

  // Configurable available sizes (centralised for future adjustment)
  const AVAILABLE_SIZES = ['M', 'L', 'XL'];

  // Optional automatic appearance configuration
  const AUTO_POPUP_CONFIG = {
    enabled: false, // Automatically opens first when customer enters collection page
    delayMs: 600,
    storageKey: 'ekkomi_waitlist_dismissed'
  };

  // Backend API Configuration (Local Dev & Hosted Supabase Edge Function)
  // Backend API Configuration — Supabase Edge Function
  const BACKEND_CONFIG = {
    supabaseEndpoint:
      'https://chjzsdnypkllihdzokhg.supabase.co/functions/v1/waitlist',

    getEndpoint: function () {
      return this.supabaseEndpoint;
    }
  };

  // Future Shopify Configuration & Variant Mapping
  const SHOPIFY_CONFIG = {
    enabled: false, // Set to true when Shopify store and payments are live
    storeDomain: 'ekkomi.myshopify.com',
    products: {
      men: {
        curiosity: { title: 'Curiosity - Dark Navy', productId: 'gid://shopify/Product/101', variants: { XS: 'var_m_cur_xs', S: 'var_m_cur_s', M: 'var_m_cur_m', L: 'var_m_cur_l', XL: 'var_m_cur_xl', XXL: 'var_m_cur_xxl' } },
        temptation: { title: 'Temptation - Forest Green', productId: 'gid://shopify/Product/102', variants: { XS: 'var_m_tem_xs', S: 'var_m_tem_s', M: 'var_m_tem_m', L: 'var_m_tem_l', XL: 'var_m_tem_xl', XXL: 'var_m_tem_xxl' } },
        desire: { title: 'Desire - Deep Red', productId: 'gid://shopify/Product/103', variants: { XS: 'var_m_des_xs', S: 'var_m_des_s', M: 'var_m_des_m', L: 'var_m_des_l', XL: 'var_m_des_xl', XXL: 'var_m_des_xxl' } },
        audacity: { title: 'Audacity - Deep Mustard', productId: 'gid://shopify/Product/104', variants: { XS: 'var_m_aud_xs', S: 'var_m_aud_s', M: 'var_m_aud_m', L: 'var_m_aud_l', XL: 'var_m_aud_xl', XXL: 'var_m_aud_xxl' } },
        insolence: { title: 'Insolence - Black', productId: 'gid://shopify/Product/105', variants: { XS: 'var_m_ins_xs', S: 'var_m_ins_s', M: 'var_m_ins_m', L: 'var_m_ins_l', XL: 'var_m_ins_xl', XXL: 'var_m_ins_xxl' } }
      },
      women: {
        curiosity: { title: 'Curiosity - Dark Navy', productId: 'gid://shopify/Product/201', variants: { XS: 'var_w_cur_xs', S: 'var_w_cur_s', M: 'var_w_cur_m', L: 'var_w_cur_l', XL: 'var_w_cur_xl', XXL: 'var_w_cur_xxl' } },
        desire: { title: 'Desire - Deep Red', productId: 'gid://shopify/Product/202', variants: { XS: 'var_w_des_xs', S: 'var_w_des_s', M: 'var_w_des_m', L: 'var_w_des_l', XL: 'var_w_des_xl', XXL: 'var_w_des_xxl' } },
        audacity: { title: 'Audacity - Deep Mustard', productId: 'gid://shopify/Product/203', variants: { XS: 'var_w_aud_xs', S: 'var_w_aud_s', M: 'var_w_aud_m', L: 'var_w_aud_l', XL: 'var_w_aud_xl', XXL: 'var_w_aud_xxl' } }
      }
    },
    // Hook for checking real inventory once Shopify integration is connected
    checkInventory: async function (collection, jacketKey, size) {
      if (!this.enabled) return { available: null, checked: false };
      // Future Shopify Storefront GraphQL query goes here
      return { available: true, variantId: this.products[collection]?.[jacketKey]?.variants[size] };
    }
  };

  // Jacket Definitions by Collection with Editorial Images
  const JACKET_CATALOG = {
    men: [
      { key: 'curiosity', id: 'men-curiosity', number: '01', name: 'CURIOSITY', colour: 'Dark Navy', hex: '#1c2838', inStock: false, image: 'assets/collection/nocturne/curiosity/curiosity_lookbook_1.jpg' },
      { key: 'temptation', id: 'men-temptation', number: '02', name: 'TEMPTATION', colour: 'Forest Green', hex: '#27382b', inStock: true, image: 'assets/collection/nocturne/temptation/temptation.jpg' },
      { key: 'desire', id: 'men-desire', number: '03', name: 'DESIRE', colour: 'Deep Red', hex: '#662225', inStock: false, image: 'assets/collection/nocturne/desire/desire.jpg' },
      { key: 'audacity', id: 'men-audacity', number: '04', name: 'AUDACITY', colour: 'Deep Mustard', hex: '#8c6b24', inStock: true, image: 'assets/collection/nocturne/audacity/audacity_lookbook_1.jpg' },
      { key: 'insolence', id: 'men-insolence', number: '05', name: 'INSOLENCE', colour: 'Black', hex: '#1a1716', inStock: false, image: 'assets/collection/nocturne/insolence/insolence.jpg' }
    ],
    women: [
      { key: 'curiosity', id: 'women-curiosity', number: '01', name: 'CURIOSITY', colour: 'Dark Navy', hex: '#1c2838', inStock: false, image: 'assets/collection/nocturne/curiosity/curiosity_women_1.jpg' },
      { key: 'desire', id: 'women-desire', number: '02', name: 'DESIRE', colour: 'Deep Red', hex: '#662225', inStock: false, image: 'assets/collection/nocturne/desire/desire_editorial_3.jpg' },
      { key: 'audacity', id: 'women-audacity', number: '03', name: 'AUDACITY', colour: 'Deep Mustard', hex: '#8c6b24', inStock: true, image: 'assets/collection/nocturne/audacity/audacity.jpg' }
    ]
  };

  // State
  const state = {
    isOpen: false,
    currentStep: 1,
    collection: 'men',
    jacket: null,
    size: null,
    fullName: '',
    email: '',
    phone: '',
    consent: false,
    isSubmitting: false,
    history: [1]
  };

  // DOM Elements cache
  let backdropEl = null;
  let dialogEl = null;
  let backBtn = null;
  let closeBtn = null;
  let progressEl = null;
  let steps = {};

  function init() {
    backdropEl = document.getElementById('waitlistBackdrop');
    dialogEl = document.getElementById('waitlistDialog');
    backBtn = document.getElementById('waitlistBackBtn');
    closeBtn = document.getElementById('waitlistCloseBtn');
    progressEl = document.getElementById('waitlistProgress');

    if (!backdropEl || !dialogEl) return;

    for (let i = 1; i <= 6; i++) {
      steps[i] = document.getElementById(`waitlistStep${i}`);
    }

    // Bind Controls
    if (closeBtn) closeBtn.addEventListener('click', closeWaitlist);
    if (backBtn) backBtn.addEventListener('click', goBack);

    // Backdrop click closes modal
    backdropEl.addEventListener('click', (e) => {
      if (e.target === backdropEl) {
        closeWaitlist();
      }
    });

    // Keyboard navigation (Escape key)
    document.addEventListener('keydown', (e) => {
      if (state.isOpen && e.key === 'Escape') {
        closeWaitlist();
      }
    });

    // Step 1: Continue button
    const step1Btn = document.getElementById('step1ContinueBtn');
    if (step1Btn) {
      step1Btn.addEventListener('click', () => {
        goToStep(2);
      });
    }

    // Step 2: Collection selection cards
    const collectionBtns = dialogEl.querySelectorAll('[data-collection]');
    collectionBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const col = btn.getAttribute('data-collection');
        selectCollection(col);
        goToStep(3);
      });
    });

    // Step 5: Form submission
    const form = document.getElementById('waitlistForm');
    if (form) {
      form.addEventListener('submit', handleFormSubmit);
    }

    // Step 5: Edit Pill
    const editBtn = document.getElementById('pillEditBtn');
    if (editBtn) {
      editBtn.addEventListener('click', () => {
        goToStep(2);
      });
    }

    // Step 6: Explore EKKOMI Collections
    const backToCollBtn = document.getElementById('backToCollectionBtn');
    if (backToCollBtn) {
      backToCollBtn.addEventListener('click', () => {
        closeWaitlist();
        const colSection = document.getElementById('collection');
        if (colSection) {
          colSection.scrollIntoView({ behavior: 'smooth' });
        }
      });
    }

    // Bind page-level entry buttons
    bindEntryButtons();

    // Setup optional auto popup
    setupAutoPopup();

    // Render sizes grid
    renderSizesGrid();
  }

  function bindEntryButtons() {
    // Header button
    const headerBtn = document.getElementById('headerWaitlistBtn');
    if (headerBtn) {
      headerBtn.addEventListener('click', (e) => {
        e.preventDefault();
        openWaitlist();
      });
    }

    // Hero button
    const heroBtn = document.getElementById('heroWaitlistBtn');
    if (heroBtn) {
      heroBtn.addEventListener('click', (e) => {
        e.preventDefault();
        openWaitlist();
      });
    }

    // Floating waitlist button
    const floatingBtn = document.getElementById('floatingWaitlistBtn');
    if (floatingBtn) {
      floatingBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const activeDept = window.currentSelectedDepartment || document.body.dataset.activeDepartment || 'men';
        const activeJacket = window.userHasSelectedJacket ? (window.currentSelectedJacket || null) : null;

        openWaitlist({
          collection: activeDept,
          jacketKey: activeJacket ? activeJacket.key : null,
          jacketName: activeJacket ? activeJacket.impulse : null,
          jacketNumber: activeJacket ? activeJacket.number : null,
          jacketHex: activeJacket ? activeJacket.hex : null,
          jacketColour: activeJacket ? activeJacket.colour : null,
          outOfStock: activeJacket ? (activeJacket.inStock === false) : false
        });
      });
    }

    // Document-level listener for dynamically rendered buttons (e.g. inside dynamic product showcase)
    document.addEventListener('click', (e) => {
      const target = e.target.closest('#showcaseWaitlistBtn, .btn-join-waitlist, [data-open-waitlist]');
      if (target) {
        e.preventDefault();
        // If customer is viewing a specific jacket, preselect it!
        const activeDept = window.currentSelectedDepartment || document.body.dataset.activeDepartment || 'men';
        const activeJacket = window.currentSelectedJacket || null;

        openWaitlist({
          collection: activeDept,
          jacketKey: activeJacket ? activeJacket.key : null,
          jacketName: activeJacket ? activeJacket.impulse : null,
          jacketNumber: activeJacket ? activeJacket.number : null,
          jacketHex: activeJacket ? activeJacket.hex : null,
          jacketColour: activeJacket ? activeJacket.colour : null
        });
      }
    });
  }

  function setupAutoPopup() {
    // Check URL parameters for deep-linking or instant step navigation (e.g. ?step=4 or ?step=5)
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const stepParam = parseInt(urlParams.get('step') || urlParams.get('waitlist_step'), 10);
      if (stepParam && stepParam >= 1 && stepParam <= 6) {
        setTimeout(() => {
          openWaitlist({ collection: urlParams.get('col') || 'men', jacketKey: urlParams.get('jacket') || 'desire' });
          goToStep(stepParam, false);
        }, 80);
        return;
      }
    } catch (e) { }

    if (!AUTO_POPUP_CONFIG.enabled) return;
    // Show first when customer opens the collection page
    setTimeout(() => {
      if (!state.isOpen) {
        openWaitlist();
      }
    }, AUTO_POPUP_CONFIG.delayMs);
  }

  let previouslyFocusedElement = null;

  function openWaitlist(preselects = {}) {
    if (state.isOpen && !preselects.collection && !preselects.jacketKey) {
      return;
    }
    try {
      previouslyFocusedElement = document.activeElement;
      const scrollbarWidth = window.innerWidth - document.documentElement.clientWidth;
      if (scrollbarWidth > 0) {
        document.body.style.paddingRight = `${scrollbarWidth}px`;
      }
    } catch (e) { }

    state.isOpen = true;
    state.outOfStock = !!preselects.outOfStock;
    document.body.classList.add('waitlist-open');

    // Preselect collection if passed or keep existing
    if (preselects.collection && (preselects.collection === 'men' || preselects.collection === 'women')) {
      selectCollection(preselects.collection, false);
    }

    // Preselect jacket if passed
    if (preselects.jacketKey) {
      const catalog = JACKET_CATALOG[state.collection] || [];
      const found = catalog.find(j => j.key === preselects.jacketKey);
      if (found) {
        state.jacket = found;
      }
    }

    // Reset to Step 1 by default, or Step 4 if both collection and jacket are already chosen
    if (preselects.jacketKey && preselects.collection) {
      state.history = [1, 2, 3];
      goToStep(4, false);
    } else {
      state.history = [1];
      goToStep(1, false);
    }

    backdropEl.classList.add('is-active');
    backdropEl.setAttribute('aria-hidden', 'false');

    // Focus first interactive element for keyboard accessibility
    setTimeout(() => {
      const firstFocusable = dialogEl.querySelector('button:not([disabled]), input:not([disabled])');
      if (firstFocusable) firstFocusable.focus();
    }, 150);
  }

  function closeWaitlist() {
    state.isOpen = false;
    document.body.classList.remove('waitlist-open');
    document.body.style.paddingRight = '';
    backdropEl.classList.remove('is-active');
    backdropEl.setAttribute('aria-hidden', 'true');

    if (previouslyFocusedElement && typeof previouslyFocusedElement.focus === 'function') {
      try { previouslyFocusedElement.focus(); } catch (e) { }
    }

    // Remember dismissal
    try {
      localStorage.setItem(AUTO_POPUP_CONFIG.storageKey, 'true');
    } catch (e) { }
  }

  function goToStep(stepNum, pushHistory = true) {
    if (stepNum < 1 || stepNum > 6) return;

    if (pushHistory && state.currentStep !== stepNum) {
      state.history.push(stepNum);
    }

    state.currentStep = stepNum;

    // Show / hide step containers
    for (let i = 1; i <= 6; i++) {
      if (steps[i]) {
        if (i === stepNum) {
          steps[i].classList.remove('is-hidden');
        } else {
          steps[i].classList.add('is-hidden');
        }
      }
    }

    // Update Header Controls: Back button visible on steps 2-5
    if (backBtn) {
      if (stepNum >= 2 && stepNum <= 5) {
        backBtn.classList.remove('is-hidden');
      } else {
        backBtn.classList.add('is-hidden');
      }
    }

    // Update Progress Indicator
    if (progressEl) {
      if (stepNum >= 1 && stepNum <= 5) {
        progressEl.classList.remove('is-hidden');
        const dots = progressEl.querySelectorAll('.progress-dot');
        dots.forEach(dot => {
          const dStep = parseInt(dot.getAttribute('data-step'), 10);
          dot.classList.toggle('is-active', dStep === stepNum);
          dot.classList.toggle('is-completed', dStep < stepNum);
        });
      } else {
        progressEl.classList.add('is-hidden');
      }
    }

    // Step-specific renders
    if (stepNum === 2) {
      syncCollectionUI();
    } else if (stepNum === 3) {
      renderJacketsList();
    } else if (stepNum === 4) {
      syncSizesUI();
    } else if (stepNum === 5) {
      syncSummaryPill();
    }

    // Smooth focus
    setTimeout(() => {
      const activeStep = steps[stepNum];
      if (activeStep) {
        const focusable = activeStep.querySelector('button:not([disabled]), input:not([disabled])');
        if (focusable) focusable.focus();
      }
    }, 100);
  }

  function goBack() {
    if (state.history.length > 1) {
      state.history.pop(); // Remove current
      const prevStep = state.history[state.history.length - 1] || 1;
      goToStep(prevStep, false);
    } else {
      goToStep(1, false);
    }
  }

  function selectCollection(col, reRender = true) {
    state.collection = col;
    // If the jacket currently selected does not exist in this collection (e.g. Insolence in women), clear it
    if (state.jacket) {
      const available = JACKET_CATALOG[col].some(j => j.key === state.jacket.key);
      if (!available) {
        state.jacket = null;
      }
    }
    if (reRender) {
      syncCollectionUI();
    }
  }

  function syncCollectionUI() {
    const cards = dialogEl.querySelectorAll('[data-collection]');
    cards.forEach(card => {
      const isSelected = card.getAttribute('data-collection') === state.collection;
      card.classList.toggle('is-selected', isSelected);
      card.setAttribute('aria-checked', isSelected ? 'true' : 'false');
    });
  }

  function renderJacketsList() {
    const listEl = document.getElementById('waitlistJacketsList');
    const labelEl = document.getElementById('summaryCollectionLabel');
    if (!listEl) return;

    if (labelEl) {
      labelEl.textContent = state.collection === 'men' ? "MEN'S COLLECTION" : "WOMEN'S COLLECTION";
    }

    const jackets = JACKET_CATALOG[state.collection] || [];

    listEl.innerHTML = jackets.map(j => {
      const isSelected = state.jacket && state.jacket.key === j.key;
      return `
        <button type="button"
                class="waitlist-jacket-card${isSelected ? ' is-selected' : ''}"
                data-jacket-key="${j.key}"
                role="radio"
                aria-checked="${isSelected ? 'true' : 'false'}">
          <div class="jacket-card-left">
            ${j.image ? `
              <div class="jacket-thumb-wrapper">
                <img src="${j.image}" alt="${j.name} jacket" class="jacket-thumb-img" loading="eager" decoding="async">
              </div>
            ` : ''}
            <span class="jacket-swatch" style="background-color: ${j.hex};" aria-hidden="true"></span>
            <div class="jacket-meta">
              <span class="jacket-number">${j.number}</span>
              <span class="jacket-name">${j.name}</span>
            </div>
          </div>
          
        </button>
      `;
    }).join('');

    // Bind jacket card clicks
    const cards = listEl.querySelectorAll('[data-jacket-key]');
    cards.forEach(card => {
      card.addEventListener('click', () => {
        const key = card.getAttribute('data-jacket-key');
        const jacket = jackets.find(j => j.key === key);
        if (jacket) {
          state.jacket = jacket;
          // Visual selection feedback
          cards.forEach(c => c.classList.remove('is-selected'));
          card.classList.add('is-selected');
          setTimeout(() => {
            goToStep(4);
          }, 180);
        }
      });
    });
  }

  function renderSizesGrid() {
    const gridEl = document.getElementById('waitlistSizesGrid');
    if (!gridEl) return;

    gridEl.innerHTML = AVAILABLE_SIZES.map(s => `
      <button type="button"
              class="waitlist-size-btn"
              data-size="${s}"
              role="radio"
              aria-checked="false">
        ${s}
      </button>
    `).join('');

    const sizeBtns = gridEl.querySelectorAll('[data-size]');
    sizeBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const size = btn.getAttribute('data-size');
        state.size = size;
        sizeBtns.forEach(b => b.classList.remove('is-selected'));
        btn.classList.add('is-selected');
        setTimeout(() => {
          goToStep(5);
        }, 180);
      });
    });
  }

  function syncSizesUI() {
    const jacketLabel = document.getElementById('summaryJacketLabel');
    const sizeSubtitle = document.getElementById('step4Subtitle');
    if (sizeSubtitle) {
      if (state.outOfStock) {
        sizeSubtitle.textContent = 'This piece is currently unavailable. Select your size to join the waiting list.';
      } else {
        sizeSubtitle.textContent = 'Select your size to join the waiting list.';
      }
    }
    if (jacketLabel && state.jacket) {
      jacketLabel.textContent = state.jacket.name;
    }

    const sizeBtns = dialogEl.querySelectorAll('[data-size]');
    sizeBtns.forEach(btn => {
      const isSelected = btn.getAttribute('data-size') === state.size;
      btn.classList.toggle('is-selected', isSelected);
      btn.setAttribute('aria-checked', isSelected ? 'true' : 'false');
    });
  }

  function syncSummaryPill() {
    const textEl = document.getElementById('pillSummaryText');
    const dotEl = document.getElementById('pillColorDot');

    if (textEl && state.jacket && state.size) {
      const colLabel = state.collection === 'men' ? 'Men' : 'Women';
      textEl.textContent = `${colLabel} · ${state.jacket.name} · Size ${state.size}`;
    }

    if (dotEl && state.jacket) {
      dotEl.style.backgroundColor = state.jacket.hex || '#773A3C';
    }
  }

  async function handleFormSubmit(e) {
    e.preventDefault();
    if (state.isSubmitting) return;

    // Reset error messages
    clearErrors();

    const nameInput = document.getElementById('waitlistFullName');
    const emailInput = document.getElementById('waitlistEmail');
    const phoneInput = document.getElementById('waitlistPhone');
    const consentInput = document.getElementById('waitlistConsent');
    const submitBtn = document.getElementById('submitWaitlistBtn');
    const btnText = submitBtn ? submitBtn.querySelector('.btn-text') : null;
    const btnSpinner = submitBtn ? submitBtn.querySelector('.btn-spinner') : null;

    const fullName = nameInput ? nameInput.value.trim() : '';
    const email = emailInput ? emailInput.value.trim() : '';
    const phone = phoneInput ? phoneInput.value.trim() : '';
    const consent = consentInput ? consentInput.checked : false;

    // Validation
    let hasError = false;

    if (!fullName || fullName.length < 2) {
      showError('nameError', 'Please enter your full name.');
      hasError = true;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
      showError('emailError', 'Please enter a valid email address.');
      hasError = true;
    }

    const phoneClean = phone.replace(/[\s\-\(\)\.]/g, '');
    if (!phone || phoneClean.length < 7 || !/^(\+)?\d{7,16}$/.test(phoneClean)) {
      showError('phoneError', 'Please enter a valid phone number.');
      hasError = true;
    }

    if (!state.collection || !state.jacket || !state.size) {
      showError('generalFormError', 'Please select your collection, jacket, and size.');
      hasError = true;
    }

    if (!consent) {
      showError('consentError', 'Please confirm your consent to receive availability updates.');
      hasError = true;
    }

    if (hasError) return;

    // Build payload
    const payload = {
      fullName: fullName,
      email: email,
      phone: phone,
      collection: state.collection === 'men' ? 'Men' : 'Women',
      jacketId: state.jacket.id,
      jacketName: state.jacket.name,
      jacketColour: state.jacket.colour,
      size: state.size,
      consent: true,
      timestamp: new Date().toISOString()
    };

    // Prepare Confirmation Email Text (for backend dispatch)
    payload.confirmationEmail = generateConfirmationEmail(payload);

    // Prevent duplicate submissions & set loading state
    state.isSubmitting = true;
    if (submitBtn) submitBtn.disabled = true;
    if (btnText) btnText.textContent = 'REGISTERING...';
    if (btnSpinner) btnSpinner.classList.remove('is-hidden');

    try {
      let isSuccess = false;
      let errorMessage = 'Unable to complete your registration. Please try again.';

      // Anti-Spam Honeypot Check
      const honeypotInput = document.getElementById('waitlistHoneypot');
      if (honeypotInput && honeypotInput.value) {
        payload.b_company_url = honeypotInput.value;
      }

      // Save a local draft so if there is a network drop, details are not lost
      try {
        localStorage.setItem('ekkomi_waitlist_draft', JSON.stringify({
          collection: payload.collection,
          jacketKey: state.jacket ? state.jacket.key : null,
          size: payload.size,
          fullName: payload.fullName,
          email: payload.email,
          phone: payload.phone
        }));
      } catch (storageErr) { }

      // Attempt to post to real backend endpoint
      const endpoint = BACKEND_CONFIG.getEndpoint();
      try {
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        });

        const resData = await response.json().catch(() => ({}));

        if (response.ok && resData.success) {
          isSuccess = true;
          state.registrationId = resData.registrationId;
          console.log('[WAITLIST] Confirmed by backend:', resData);
        } else {
          errorMessage = resData.error || 'Registration could not be completed at this time. Please verify your details.';
          console.warn('[WAITLIST] Backend returned error:', resData);
        }
      } catch (netErr) {
        console.warn('[WAITLIST] Network connection error:', netErr);
        errorMessage = 'Unable to reach the server. Please check your connection and retry.';
      }

      // Show success ONLY after backend confirms the registration
      if (isSuccess) {
        if (nameInput) nameInput.value = '';
        if (emailInput) emailInput.value = '';
        if (phoneInput) phoneInput.value = '';
        if (consentInput) consentInput.checked = false;

        try {
          localStorage.removeItem('ekkomi_waitlist_draft');
        } catch (e) { }

        goToStep(6, false);
      } else {
        // Keep customer details intact and show specific error
        showError('generalFormError', errorMessage);
      }
    } catch (err) {
      console.error('[WAITLIST ERROR]', err);
      showError('generalFormError', 'A system error occurred. Please try again.');
    } finally {
      state.isSubmitting = false;
      if (submitBtn) submitBtn.disabled = false;
      if (btnText) btnText.textContent = 'JOIN THE WAITING LIST';
      if (btnSpinner) btnSpinner.classList.add('is-hidden');
    }
  }

  function generateConfirmationEmail(data) {
    return {
      to: data.email,
      subject: 'Your EKKOMI NOCTURNE Waiting List Confirmation',
      body: `Thank you for joining the EKKOMI NOCTURNE waiting list.\n\nWe've successfully received your request for the following piece:\n\nCollection: ${data.collection}\nJacket: ${data.jacketName}\nSize: ${data.size}\n\nWe'll notify you about your selected jacket's availability.\n\nThank you for your interest in EKKOMI.\n\nEKKOMI`
    };
  }

  function showError(elementId, msg) {
    const el = document.getElementById(elementId);
    if (el) {
      el.textContent = msg;
      el.classList.add('is-visible');
    }
  }

  function clearErrors() {
    const errors = dialogEl.querySelectorAll('.waitlist-error, .waitlist-form-error');
    errors.forEach(e => {
      e.textContent = '';
      e.classList.remove('is-visible');
    });
  }

  // Initialize on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose global API
  window.EkkomiWaitlist = {
    open: openWaitlist,
    close: closeWaitlist,
    goToStep: goToStep,
    getState: () => ({ ...state }),
    shopify: SHOPIFY_CONFIG
  };

})();

