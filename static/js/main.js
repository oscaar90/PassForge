function copyToClipboard() {
    const input = document.getElementById("generated");
    input.select();
    document.execCommand("copy");

    const msg = document.getElementById("copy-msg");
    if (!msg) return;

    msg.classList.add("show");

    setTimeout(() => {
        msg.classList.remove("show");
    }, 2000);
}
