function solution(id_list, report, k) {
  var answer = new Array(id_list.length);
  answer.fill(0);
  const reportSet = new Set(report);
  const reportSetToArr = [...reportSet];
  const reportObj = {};
  id_list.forEach((id) => {
    reportObj[id] = [];
  });

  reportSetToArr.forEach((report) => {
    const [userId, reportId] = report.split(" ");
    reportObj[reportId].push(userId);
  });

  for (let key in reportObj) {
    if (reportObj[key].length >= k) {
      reportObj[key].forEach((id) => {
        answer[id_list.indexOf(id)]++;
      });
    }
  }

  return answer;
}
