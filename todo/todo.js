function addTask() {
  const taskInput = document.getElementById("task-input");
  const dateInput = document.getElementById("task-date");
  const priorityInput = document.getElementById("task-priority");
  const taskList = document.getElementById("task-list");

  const taskText = taskInput.value.trim();
  const taskDate = dateInput.value;
  const taskPriority = priorityInput.value;

  if (taskText === "" || taskDate === "") {
    alert("Isi tugas dan tanggal terlebih dahulu!");
    return;
  }

  const row = document.createElement("tr");

  row.innerHTML = `
    <td>${taskText}</td>
    <td>${new Date(taskDate).toLocaleString()}</td>
    <td class="priority-${taskPriority.replace(" ", "\\ ")}">${taskPriority}</td>
    <td>
      <button class="action-btn complete-btn" onclick="completeTask(this)">Selesai</button>
      <button class="action-btn delete-btn" onclick="deleteTask(this)">Hapus</button>
    </td>
  `;

  taskList.appendChild(row);

  taskInput.value = "";
  dateInput.value = "";
  priorityInput.value = "Urgent";
}

function completeTask(btn) {
  const row = btn.parentElement.parentElement;
  row.classList.toggle("completed");
}

function deleteTask(btn) {
  const row = btn.parentElement.parentElement;
  row.remove();
}
