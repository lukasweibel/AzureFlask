async function handleAddition(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const a = formData.get('a');
    const b = formData.get('b');
    const response = await fetch(`/add?a=${a}&b=${b}`);
    const result = await response.json();
    document.getElementById('result').textContent = `Sum: ${result.sum}`;
}