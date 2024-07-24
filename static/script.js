async function generateShayari() {
    const keyword = document.getElementById('keyword').value;
    if (!keyword) {
        alert('Please enter a keyword');
        return;
    }

    try {
        const response = await fetch(`/generate-shayari?keyword=${encodeURIComponent(keyword)}`);
        const data = await response.json();

        if (response.ok) {
            document.getElementById('shayari').innerText = data.shayari;
        } else {
            document.getElementById('shayari').innerText = `Error: ${data.error}`;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('shayari').innerText = 'An error occurred while fetching the Shayari';
    }
}
