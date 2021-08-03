#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  const last = list.length - 1;

  for (let increment = last; increment >= 0; increment--) {
    reverseList.push(list[increment]);
  }
  return (reverseList);
};
