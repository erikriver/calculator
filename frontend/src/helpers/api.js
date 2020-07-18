//  Send a requests to the server and get the result as a promise
export default function api(number1, number2, operator) {
  var data = {
    number1: number1,
    number2: number2,
    operator: operator,
  };

  return fetch("/api", {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      return response.json();
    })
    .then((result) => {
      return result.msg;
    });
}
