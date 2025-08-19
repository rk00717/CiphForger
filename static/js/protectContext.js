export function protectContext() {
    window.onkeydown = (e) => {
        if((e.keyCode == 123) 
            || (e.ctrlKey && e.keyCode == 'S'.charCodeAt(0))
        || (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0))
        || (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0))
        || (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0))
        || (e.ctrlKey && e.keyCode == 'P'.charCodeAt(0))
        || (e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0))){
            return false;
        }
    }

    window.addEventListener("contextmenu", (e) => {
        e.preventDefault();
    })
}