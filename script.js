// Add an event listener to the "Generate Content" button
document.getElementById('submitBtn').addEventListener('click', async () => {
    // Get the value from the course title input field
    const courseTitle = document.getElementById('courseTitle').value;

    // Get the output div where the generated content will be displayed
    const output = document.getElementById('output');

    // Display a loading message while the content is being generated
    output.innerHTML = '<p>Loading...</p>';

    try {
        // Make a POST request to the '/generate-content' endpoint with the course title as the body
        const response = await fetch('/generate-content', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ courseTitle })
        });

        // Parse the JSON response from the server
        const data = await response.json();

        // Check if the content was generated successfully
        if (data.content) {
            const content = data.content;

            // Display the generated content in the output div and add a "Copy to Clipboard" button
            output.innerHTML = `<pre>${content}</pre><button id="copyBtn">Copy to Clipboard</button>`;

            // Add an event listener to the "Copy to Clipboard" button
            document.getElementById('copyBtn').addEventListener('click', () => {
                // Copy the generated content to the clipboard
                navigator.clipboard.writeText(content);

                // Alert the user that the content has been copied
                alert('Content copied to clipboard!');
            });
        } else {
            // Display an error message if no content was generated
            output.innerHTML = '<p>Error generating content. Please try again.</p>';
        }
    } catch (error) {
        // Display an error message if the content generation fails
        output.innerHTML = '<p>Error generating content. Please try again.</p>';
        
        // Log the error to the console for debugging purposes
        console.error(error);
    }
});
