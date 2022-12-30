const squares = (x) => x * x;

const cubes = (x) => x * x * x;

const sumSquares = (a, b) => {
  // returns sum of squares of numbers starting from a to b
  if (a > b) return 0;
  return (a * a) + sumSquares(a + 1, b);
};
/*
 * > sumSquares(3,5)
 * 50
 */

const sumCubes = (a, b) => {
  if (a > b) return 0;
  return (a * a * a) + sumCubes(a + 1, b);
};
/*
 * > sumCubes(3,5)
 * 216 
 */

// higher order function which takes a function as a formal argument

const sum = (fn,a,b) => {
  if(a > b) return 0;
  return (fn(a)) + sum(fn, a+1, b);
}

/*
 * > sum(squares,3,5)
 * 50
 * > sum(cubes,3,5)
 * 216
 */

 // checks for the words containing the check word in the given sentence and returns them 
function checkWord(sentence, check) {
  let arr = sentence.split(' ');
  let words = '';
  arr.forEach(word => {
    if(word.includes(check)) {
      words += ' ' + word;
    }
  })
  words = words.trim();
  return words;
}
/*
 * > checkWord('A lot of garbage is on the streets someone needs to go and clean the streets','e')
 * "garbage the streets someone needs clean the streets"

