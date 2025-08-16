const input = document.getElementById("task-input");
const list = document.getElementById("task-list");

function addTask() {
  if (input.value.trim() === "") return;

  const li = document.createElement("li");
  li.innerHTML = `
    <span onclick="toggleTask(this)">${input.value}</span>
    <button class="delete" onclick="deleteTask(this)">X</button>
  `;
  list.appendChild(li);
  input.value = "";
}

function toggleTask(el) {
  el.parentElement.classList.toggle("done");
  if (el.parentElement.classList.contains("done")) {
    launchConfetti();
  }
}

function deleteTask(el) {
  el.parentElement.remove();
}

// Confetti effect
function launchConfetti() {
  for (let i = 0; i < 15; i++) {
    const confetti = document.createElement("div");
    confetti.classList.add("confetti");
    document.body.appendChild(confetti);
    confetti.style.left = Math.random() * window.innerWidth + "px";
    confetti.style.background = `hsl(${Math.random() * 360}, 100%, 70%)`;
    setTimeout(() => confetti.remove(), 3000);
  }
}
