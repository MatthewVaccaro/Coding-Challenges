// function frameGenerator(n) {
// 	const restuls = [];
// 	let start = '*';
// 	let space = ' ';

// 	for (let i = 0; i < n; i++) {
// 		if (i == 0 || i == n - 1) {
// 			let startCount = start.repeat(n);
// 			restuls.push(startCount);
// 		}
// 		else {
// 			let spaceCount = space.repeat(n - 2);
// 			restuls.push('*' + spaceCount + '*');
// 		}
// 	}

// 	return restuls;
// }

function frameGenerator(n) {
	const array = [];

	if (array.length === 0) {
		return None;
	}

	if (array.length <= 2) {
		for (i = 0; i < array.length; i++) {
			return array[''];
		}
	}

	if (arr.length > 2) {
		for (i = 0; i < array.length - 1; i++) {
			return array[''];
		}
	}
}
return array.toString();

console.log(frameGenerator(0));
