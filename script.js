document.getElementById("generateButton").addEventListener("click", generateImage);

function generateImage() {
    const promptText = document.getElementById("prompt").value;

    if (!promptText) {
        alert("Please enter a prompt to generate the image!");
        return;
    }

    // Create the body of the payload with the prompt as a stringified object
    const payload = {
        body: JSON.stringify({ prompt: promptText })  // Stringify the object with prompt
    };

    // Call the API using POST method
    fetch('https://mqp54g1ghc.execute-api.us-east-1.amazonaws.com/Prod/generateImage', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',  // Ensure the content type is JSON
        },
        body: JSON.stringify(payload)  // The whole payload is stringified, including the "body" tag
    })
    .then(response => response.json())
    .then(data => {
        if (data.statusCode === 200) {
            // Parse the body to extract the presigned URL
            const presignedUrl = JSON.parse(data.body).presigned_url;
            displayImage(presignedUrl);
        } else {
            alert("Error: " + JSON.stringify(data.body));
        }
    })
    .catch(error => {
        console.error("Error generating image:", error);
        alert("Something went wrong. Please try again later.");
    });
}

function displayImage(url) {
    const imageContainer = document.getElementById("imageContainer");
    imageContainer.innerHTML = `<img src="${url}" alt="Generated Image">`;
}
