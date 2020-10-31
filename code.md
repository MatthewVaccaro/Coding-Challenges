### Reading Through the problem:
Key things to understand when readng through a problem
- What data type am my being given per arrgument? (string, int, list, set, dict...)
- What am I garenteed with that arrgument? (len, negitive, big, small)
- What is the required output data type (string, int, list, set, dict...)

When you don't understand what the problem is asking for:
- Look at multiple tests and try to compare the input to the output.
- Re-read the question, slowly, and always out loud

# Every questions is minpulating data - this can mean mutating, creating, sorting, adding, subtracting and so on

### Once you understand the problem
### Javascript
If you need to touch every item in a list once consider: 
- a Map / Filter / For Loop:
Map: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
^^^ Great if you need to create a new array while iterating over an array
Filter: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map
^^^ Great for comparing an item to each item being looped over
For Loop: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for
^^^ Great for when you're using an index - REMEMEBER a For loop is just incrementing or decromenting a number. Its not physical going through the items

If you need to change data time:


## String to Other
String -> Int
parseInt(stringValue)
parseInt: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt
^^^ note this does not need dot notation

----------------------------------------------------------------------------------------------------------------------------------------------------------------

String -> Array:
string.split(' ')
split: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split
^^^ add .split() to any string value and in the parentheses add a value to split on. If you want each word make sure your quotes have a space. If you want each letter remove the space. If you want to split on a symbal add the symble in the quotes.
const url = 'https://twitter.com/messages/19047593-3061847840
Example: url.split('/')  
result: ['https:', 'twitter.com' , 'messages' , '19047593-3061847840']

----------------------------------------------------------------------------------------------------------------------------------------------------------------

String -> Object:
There is no method that will do this. You would need to iterate of the string value one at time and create the object by hand

----------------------------------------------------------------------------------------------------------------------------------------------------------------

## Int to others

