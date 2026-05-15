""" 
const output = (function(x) {
  delete x;
  return x;
})(0)

console.log(output)
 """

def function(x):
    del x
    return x

output = function(0)
print(output)