// ===================================
// LAB 4: DARK MODE 
// ===================================

// INSTRUCTIONS:
// 1. Select the necessary DOM elements
// 2. Add an event listener to the toggle button
// 3. Implement the toggleDarkMode function
// 4. Update the icon when switching modes
// 5. BONUS: Save the preference to localStorage

// ===================================
// STEP 1: Select DOM Elements
// ===================================
// TODO: Select the theme toggle button
const themeToggleBtn = null; // Replace null with your code

// TODO: Select the theme icon element
const themeIcon = null; // Replace null with your code

// TODO: Get the <body> element
const body = null; // Replace null with your code


// ===================================
// STEP 2: Add Event Listener
// ===================================
// TODO: Add a 'click' event listener to the toggle button
// The event listener should call the toggleDarkMode function
// Your code here:




// ===================================
// STEP 3: Toggle Dark Mode Function
// ===================================
function toggleDarkMode() {
    // TODO 1: Toggle the 'dark-mode' class on the body element
    // Your code here:
    
    
    // TODO 2: Update the icon based on the current mode
    // Your code here:
    
    
    // Optional: Save the current mode to localStorage
    // This is optional - try it after completing the basic functionality!
    // Your code here (optional):
    
}


// ===================================
// STEP 4: Update Icon Function
// ===================================
function updateIcon(isDarkMode) {
    // TODO: Change the icon based on the mode
    // If dark mode: show sun icon ☀️
    // If light mode: show moon icon 🌙
    // Your code here:
    
}


// ===================================
// Optional: Load Saved Preference
// ===================================
// This function runs when the page loads
// It checks if there's a saved preference in localStorage
function loadSavedTheme() {
    // TODO (OPTIONAL): 
    // 1. Get the saved theme from localStorage
    // 2. If it exists and is 'dark', add the dark-mode class to body
    // 3. Update the icon accordingly
    // Your code here:
    
}

// Call the function when the page loads (uncomment when you implement it)
// loadSavedTheme();


// ===================================
// HELPFUL REMINDERS:
// ===================================
// DOM Selection:
//   - document.getElementById('id')
//   - document.querySelector('#id')
//   - document.body

// Class Manipulation:
//   - element.classList.add('class-name')
//   - element.classList.remove('class-name')
//   - element.classList.toggle('class-name')
//   - element.classList.contains('class-name')

// Event Listeners:
//   - element.addEventListener('event', function)
//   - Common events: 'click', 'mouseover', 'keydown'

// Changing Content:
//   - element.textContent = 'new text'
//   - element.innerHTML = '<span>html</span>'

// localStorage (BONUS):
//   - localStorage.setItem('key', 'value')
//   - localStorage.getItem('key')
//   - localStorage.removeItem('key')
// ===================================