// ========================================
// Analytics Workshop - Array Methods Practice
// ========================================

// Dataset
const analyticsData = [
    { 
      name: "Alice", 
      totalSessions: 3, 
      avgSessionDuration: 180 
    },
    { 
      name: "Bob", 
      totalSessions: 5, 
      avgSessionDuration: 240 
    },
    { 
      name: "Charlie", 
      totalSessions: 2, 
      avgSessionDuration: 90 
    },
    { 
      name: "Diana", 
      totalSessions: 7, 
      avgSessionDuration: 300 
    }
  ];
  
  // ========================================
  // TODO FUNCTIONS - Students implement these
  // ========================================
  
  /**
   * 1. Conditionals
   * Return "Good" if avgSessionDuration >= 200, otherwise "Low"
   * @param {Object} user - User object with avgSessionDuration property
   * @returns {string} "Good" or "Low"
   */
  const getEngagementLevel = (user) => {
    // TODO: use if/else or ternary operator
    // Hint: Check if user.avgSessionDuration >= 200
  };
  
  /**
   * 2. For Loop
   * Find the user with the longest avgSessionDuration
   * @param {Array} data - Array of user objects
   * @returns {string} Name of user with longest session
   */
  const findLongestSessionUser = (data) => {
    // TODO: use for loop
    // Hint: Keep track of max duration and corresponding user name
  };
  
  /**
   * 3. Map
   * Format each user's session count
   * @param {Array} data - Array of user objects
   * @returns {Array} Array of formatted strings like "Alice: 3 sessions"
   */
  const formatSessions = (data) => {
    // TODO: use map
    // Hint: Use template literal `${user.name}: ${user.totalSessions} sessions`
  };
  
  /**
   * 4. Filter
   * Get names of users with >= 5 sessions
   * @param {Array} data - Array of user objects
   * @returns {Array} Array of active user names
   */
  const getActiveUsers = (data) => {
    // TODO: use filter + map
    // Hint: First filter users with totalSessions >= 5, then map to get names
  };
  
  /**
   * 5. Reduce
   * Calculate total sessions across all users
   * @param {Array} data - Array of user objects
   * @returns {number} Sum of all totalSessions
   */
  const getTotalSessions = (data) => {
    // TODO: use reduce
    // Hint: Accumulate user.totalSessions
  };
  
  // ========================================
  // UI Functions (Already implemented)
  // ========================================
  
  const output = document.getElementById('output');
  
  const appendOutput = (text) => {
    output.textContent += text + '\n';
  };
  
  const clearOutput = () => {
    output.textContent = '';
  };
  
  // Display raw data
  document.getElementById('raw-data').textContent = JSON.stringify(analyticsData, null, 2);
  
  // Button handlers
  const runEngagementLevel = () => {
    clearOutput();
    appendOutput('=== Engagement Levels ===\n');
    analyticsData.forEach(user => {
      const level = getEngagementLevel(user);
      appendOutput(`${user.name} engagement: ${level}`);
    });
  };
  
  const runLongestSession = () => {
    const longest = findLongestSessionUser(analyticsData);
    appendOutput(`\n🏆 Longest session user: ${longest}`);
  };
  
  const runFormatSessions = () => {
    const formatted = formatSessions(analyticsData);
    appendOutput(`\n📝 Sessions formatted: ${JSON.stringify(formatted, null, 2)}`);
  };
  
  const runActiveUsers = () => {
    const active = getActiveUsers(analyticsData);
    appendOutput(`\n🔥 Active users (≥5): ${JSON.stringify(active)}`);
  };
  
  const runTotalSessions = () => {
    const total = getTotalSessions(analyticsData);
    appendOutput(`\n📊 Total sessions: ${total}`);
  };
  
  const reset = () => {
    clearOutput();
  };
  