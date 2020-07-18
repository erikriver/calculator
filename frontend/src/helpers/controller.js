import api from "./api";

// A block of code designed to interact with the API and view
export default function calculator(obj, buttonName) {
  // To avoid frameworks and unnecessary libraries I am using Promises
  // to handle asynchronous API calls.
  return new Promise((resolve, reject) => {

    if (buttonName === "C") {
      return resolve({
        total: null,
        next: null,
        operation: null,
      });
    }

    // if is number
    if (/\d+/.test(buttonName)) {
      if (buttonName === "0" && obj.next === "0") {
        return resolve({});
      }
      // If there is an operation, update next
      if (obj.operation) {
        if (obj.next) {
          return resolve({ next: obj.next + buttonName });
        }
        return resolve({ next: buttonName });
      }
      // If there is no operation, update next and clear the value
      if (obj.next) {
        const next = obj.next === "0" ? buttonName : obj.next + buttonName;
        return resolve({
          next,
          total: null,
        });
      }

      return resolve({
        next: buttonName,
        total: null,
      });
    }

    // An improvement for lazy people who don't put a 0 before '.'
    if (buttonName === ".") {
      if (obj.next) {
        // ignore a . if the next number already has one
        if (obj.next.includes(".")) {
          return resolve({});
        }
        return resolve({ next: obj.next + "." });
      }
      return resolve({ next: "0." });
    }

    // Validate if there are operation and values
    if (buttonName === "=") {
      if (obj.next && obj.operation) {
        return api(obj.total, obj.next, obj.operation).then((result) => {
          return resolve({
            total: result,
            next: null,
            operation: null,
          });
        });
      } else {
        // '=' with no operation, nothing to do
        return resolve({});
      }
    }

    // User pressed an operation button and there is an existing operation
    if (obj.operation) {
      return api(obj.total, obj.next, obj.operation).then((result) => {
        return resolve({
          total: result,
          next: null,
          operation: buttonName,
        });
      });
    }

    // The user hasn't typed a number yet, just save the operation
    if (!obj.next) {
      return resolve({ operation: buttonName });
    }

    // save the operation and shift 'next' into 'total'
    return resolve({
      total: obj.next,
      next: null,
      operation: buttonName,
    });
  });
}
