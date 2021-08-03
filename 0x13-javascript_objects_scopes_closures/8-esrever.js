#!/usr/bin/node

exports.esrever = function (list) {
  const reverse_list = [];
  const last = list.length - 1;

  for (let increment = last; increment >= 0; increment--) {
    reverse_list.push(list[increment]);
  }
  return (reverse_list);
};
