#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return (list.filter(sub_list => sub_list === searchElement).length);
};
