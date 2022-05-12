function solution(new_id) {
  var answer = "";
  answer = new_id;
  // 1단계: 소문자
  answer = answer.toLowerCase();
  const ansArr = [...answer];
  const allowedArray = [
    "~",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "=",
    "+",
    "[",
    "{",
    "]",
    "}",
    ":",
    "?",
    ",",
    "<",
    ">",
    "/",
  ];

  // 2단계
  for (i = 0; i < ansArr.length; i++) {
    if (allowedArray.includes(ansArr[i])) {
      ansArr.splice(i, 1);
      i--;
    }
  }
  // 3단계
  for (i = 0; i < ansArr.length - 1; i++) {
    if (ansArr[i] === "." && ansArr[i + 1] === ".") {
      ansArr.splice(i, 1);
      i--;
    }
  }
  // 4단계
  if (ansArr[0] === ".") {
    ansArr.splice(0, 1);
  }
  if (ansArr[ansArr.length - 1] === ".") {
    ansArr.splice(ansArr.length - 1, 1);
  }
  // 5단계
  if (!ansArr.length) {
    ansArr.push("a");
  }
  // 6단계
  if (ansArr.length >= 16) {
    ansArr.splice(15);
  }
  if (ansArr[ansArr.length - 1] === ".") {
    ansArr.splice(ansArr.length - 1, 1);
  }
  // 7단계
  if (ansArr.length <= 2) {
    while (ansArr.length < 3) {
      ansArr.push(ansArr[ansArr.length - 1]);
    }
  }
  answer = "";
  answer = ansArr.join("");

  return answer;
}
