var unsortedArr = [9, 10, 5, 11, 30, 55, 60, 1];

var swapped;

function bubbleSort(arr) {
   swapped = false;
   var end = arr.length - 1;
   for (var i = 0; i < end; i++){
      if (arr[i] > arr[i + 1]) {
         swapped = true;
         var temp = arr[i];
         arr[i] = arr[i + 1];
         arr[i + 1] = temp;
      }
   }
   end--;
}

do {
   bubbleSort(unsortedArr);
} while (swapped)

console.log(unsortedArr)