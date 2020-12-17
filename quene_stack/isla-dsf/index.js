/**
 * @param {character[][]} grid
 * @return {number}
 */

var grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]];


  
var numIslands = function(grid) {
    const row = grid.length;
    const col = grid[0].length;
    let islands = 0;

    for ( let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (grid[i][j] == 1) {
                console.log('add', i , j)
                islands++
                grid[i][j] = 2;
                
                bsfIslands(grid, row, col, i, j);
            }
        }
    }  
    return islands; 
};

var bsfIslands = function(grid, row, col, i, j) {
    // 遍历上面的
    if (i - 1 >= 0 && grid[i-1][j] == 1) { 
        grid[i-1][j] = 2;
        bsfIslands(grid, row, col, i-1, j);
    }

    // 遍历右边的
    if (j + 1 < col && grid[i][j+1] == 1) {
        grid[i][j + 1] = 2;
        bsfIslands(grid, row, col, i, j+1);
    } 
    // 遍历下面的
    if (i + 1 < row && grid[i+1][j] == 1) {
        grid[i+1][j] = 2;
        bsfIslands(grid, row, col, i + 1, j);
    } 
    // 遍历左边
    if (j - 1 >= 0 && grid[i][j-1] == 1) { 
        // console.log('遍历左边', grid[i][j-1] )
        grid[i][j-1] = 2;
        bsfIslands(grid, row, col, i, j - 1);
    }
    return;  
}


console.log(numIslands(grid))