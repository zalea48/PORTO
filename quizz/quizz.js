const questions = [
    { question: "Planet terbesar di tata surya?", choices: ["Bumi", "Jupiter", "Saturnus", "Neptunus"], answer: "Jupiter" },
    { question: "Bahasa pemrograman yang dipakai untuk web interaktif?", choices: ["Python", "JavaScript", "C++", "Ruby"], answer: "JavaScript" },
    { question: "Gunung tertinggi di Indonesia?", choices: ["Semeru", "Rinjani", "Cartenz", "Merbabu"], answer: "Cartenz" },
    { question: "Siapa proklamator Indonesia?", choices: ["Soekarno & Hatta", "Jokowi & JK", "Soeharto & BJ Habibie", "Megawati & Gusdur"], answer: "Soekarno & Hatta" },
    { question: "Ibukota Jepang?", choices: ["Tokyo", "Kyoto", "Osaka", "Nagoya"], answer: "Tokyo" },
    { question: "Lambang sila pertama Pancasila?", choices: ["Bintang", "Rantai", "Pohon Beringin", "Banteng"], answer: "Bintang" },
    { question: "Siapa pencipta Facebook?", choices: ["Bill Gates", "Elon Musk", "Mark Zuckerberg", "Jeff Bezos"], answer: "Mark Zuckerberg" },
    { question: "Hewan tercepat di darat?", choices: ["Cheetah", "Singa", "Kuda", "Serigala"], answer: "Cheetah" },
    { question: "Laut terbesar di dunia?", choices: ["Atlantik", "Hindia", "Arktik", "Pasifik"], answer: "Pasifik" },
    { question: "Ibukota Kalimantan Timur?", choices: ["Samarinda", "Balikpapan", "Banjarmasin", "Pontianak"], answer: "Samarinda" }
  ];
  
  let currentQuestionIndex = 0;
  let score = 0;
  
  const questionEl = document.getElementById("question");
  const choicesEl = document.getElementById("choices");
  const nextBtn = document.getElementById("next-btn");
  const scoreContainer = document.getElementById("score-container");
  
  function showQuestion() {
    const currentQuestion = questions[currentQuestionIndex];
    questionEl.textContent = currentQuestion.question;
    choicesEl.innerHTML = "";
    nextBtn.style.display = "none";
  
    currentQuestion.choices.forEach(choice => {
      const btn = document.createElement("button");
      btn.textContent = choice;
      btn.classList.add("choice-btn");
      btn.addEventListener("click", () => selectAnswer(btn, choice));
      choicesEl.appendChild(btn);
    });
  }
  
  function selectAnswer(selectedBtn, choice) {
    const correctAnswer = questions[currentQuestionIndex].answer;
    const allButtons = document.querySelectorAll(".choice-btn");
  
    if (choice === correctAnswer) {
      selectedBtn.classList.add("correct");
      score++;
    } else {
      selectedBtn.classList.add("wrong");
      allButtons.forEach(btn => {
        if (btn.textContent === correctAnswer) {
          btn.classList.add("correct");
        }
      });
    }
  
    allButtons.forEach(btn => btn.disabled = true);
    nextBtn.style.display = "block";
  }
  
  nextBtn.addEventListener("click", () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
      showQuestion();
    } else {
      showScore();
    }
  });
  
  function showScore() {
    questionEl.textContent = "🌌 Kuis selesai!";
    choicesEl.innerHTML = "";
    nextBtn.style.display = "none";
    scoreContainer.textContent = `Skor Anda: ${score} dari ${questions.length}`;
  }
  
  showQuestion();
  