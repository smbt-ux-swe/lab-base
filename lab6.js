// Get all load and stop buttons
const loadButtons = document.querySelectorAll('.load-btn');
const stopButtons = document.querySelectorAll('.stop-btn');

// Store interval IDs
let progressInterval = null;

// ============ SPINNER LOADER ============
function startSpinner() {
    const spinner = document.getElementById('spinner');
    const loadBtn = document.querySelector('[data-loader="spinner"].load-btn');
    
    // Disable button and start animation
    loadBtn.disabled = true;
    spinner.classList.add('active');
}

function stopSpinner() {
    const spinner = document.getElementById('spinner');
    const loadBtn = document.querySelector('[data-loader="spinner"].load-btn');
    
    // Stop animation and re-enable button
    spinner.classList.remove('active');
    loadBtn.disabled = false;
}

// ============ PROGRESS BAR LOADER ============
function startProgressBar() {
    const progressWrapper = document.querySelector('.progress-wrapper');
    const progressFill = document.querySelector('.progress-fill');
    const progressText = document.getElementById('progress-text');
    const loadBtn = document.querySelector('[data-loader="progress"].load-btn');
    
    // Disable button
    loadBtn.disabled = true;
    
    // Show progress bar
    progressWrapper.classList.add('active');
    
    // Reset and start progress
    let progress = 0;
    progressFill.style.width = '0%';
    progressText.textContent = '0%';
    
    // Update progress continuously
    progressInterval = setInterval(() => {
        progress += 1;
        progressFill.style.width = progress + '%';
        progressText.textContent = progress + '%';
        
        // Loop back to 0 when reaching 100
        if (progress >= 100) {
            progress = 0;
        }
    }, 20); // Update every 20ms for smooth animation
}

function stopProgressBar() {
    const progressWrapper = document.querySelector('.progress-wrapper');
    const progressFill = document.querySelector('.progress-fill');
    const progressText = document.getElementById('progress-text');
    const loadBtn = document.querySelector('[data-loader="progress"].load-btn');
    
    // Stop interval
    if (progressInterval) {
        clearInterval(progressInterval);
        progressInterval = null;
    }
    
    // Hide and reset
    progressWrapper.classList.remove('active');
    loadBtn.disabled = false;
    
    setTimeout(() => {
        progressFill.style.width = '0%';
        progressText.textContent = '0%';
    }, 300);
}

// ============ DOTS LOADER ============
function startDotsLoader() {
    const dotsLoader = document.getElementById('dots-loader');
    const loadBtn = document.querySelector('[data-loader="dots"].load-btn');
    
    // Disable button and start animation
    loadBtn.disabled = true;
    dotsLoader.classList.add('active');
}

function stopDotsLoader() {
    const dotsLoader = document.getElementById('dots-loader');
    const loadBtn = document.querySelector('[data-loader="dots"].load-btn');
    
    // Stop animation and re-enable button
    dotsLoader.classList.remove('active');
    loadBtn.disabled = false;
}

// ============ EVENT LISTENERS ============
loadButtons.forEach(button => {
    button.addEventListener('click', (e) => {
        const loaderType = e.target.dataset.loader;
        
        switch(loaderType) {
            case 'spinner':
                startSpinner();
                break;
            case 'progress':
                startProgressBar();
                break;
            case 'dots':
                startDotsLoader();
                break;
        }
    });
});

stopButtons.forEach(button => {
    button.addEventListener('click', (e) => {
        const loaderType = e.target.dataset.loader;
        
        switch(loaderType) {
            case 'spinner':
                stopSpinner();
                break;
            case 'progress':
                stopProgressBar();
                break;
            case 'dots':
                stopDotsLoader();
                break;
        }
    });
});