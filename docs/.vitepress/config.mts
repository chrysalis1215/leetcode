import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/leetcode/',
  title: "LeetCode",
  description: "Record for LeetCode",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      // { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Dynamic Programming',
        items: [
          { text: "198.House Robber", link: 'auto/198'},
          { text: "213.House Robber II", link: 'auto/213'},
          // { text: "1422. Maximum Score After Splitting a String", link: '/auto/1422'},
          // { text: "1534. Count Good Triplets", link: '/auto/1534'},
        ]
      },
      {
        text: 'Backtracking',
        items: [
          { text: "39.Combination Sum", link: 'auto/39'},
          { text: "40.Combination Sum II", link: 'auto/40'},
          { text: "46.Permutations", link: 'auto/46'},
          { text: "47.Permutations II", link: 'auto/47'},
          // { text: "1422. Maximum Score After Splitting a String", link: '/auto/1422'},
          // { text: "1534. Count Good Triplets", link: '/auto/1534'},
        ]
      },
      {
        text: 'Classical Interview Type',
        items: [
          { text: "146.LRU Cache", link: 'auto/146'},
          // { text: "1422. Maximum Score After Splitting a String", link: '/auto/1422'},
          // { text: "1534. Count Good Triplets", link: '/auto/1534'},
        ]
      },
      {
        text: 'Linked List',
        items: [
          { text: "19.Remove Nth Node From End of List", link: 'auto/19'},
          { text: "21.Merge Two Sorted Lists", link: 'auto/21'},
          { text: "23.Merge k Sorted Lists", link: 'auto/23'},
          { text: "92.Reverse Linked List II", link: 'auto/92'},
          { text: "206.Reverse Linked List", link: 'auto/206'},
          { text: "430.Flatten a Multilevel Doubly Linked List", link: 'auto/430'},
          { text: "707.Design Linked List", link: 'auto/707'},
          // { text: "1422. Maximum Score After Splitting a String", link: '/auto/1422'},
          // { text: "1534. Count Good Triplets", link: '/auto/1534'},
        ]
      },
      {
        text: 'Prefix Sum',
        items: [
          { text: "325. Maximum Size Subarray Sum Equals k", link: '/others/array/325'},
          { text: "560. Subarray Sum Equals K", link: '/auto/560'},
          { text: "1422. Maximum Score After Splitting a String", link: '/auto/1422'},
          { text: "1534. Count Good Triplets", link: '/auto/1534'},
        ]
      },
      {
        text: 'Sliding Window',
        items: [
          { text: "3.Longest Substring Without Repeating Characters", link: '/auto/3'},
          { text: "76. Minimum Window Substring", link: '/auto/76'},
          { text: "438. Find All Anagrams in a String", link: '/auto/438'},
          { text: "567. Permutation in String", link: '/auto/567'},
          // { text: "1422. Maximum Score After Splitting a String", link: '/auto/1422'},
          // { text: "1534. Count Good Triplets", link: '/auto/1534'},
        ]
      },
      {
        text: 'Two Pointer',
        items: [
          { text: "11.Container With Most Water", link: '/auto/11'},
          { text: "15.Three Sum", link: '/auto/15'},
          { text: "16.3Sum Closest", link: '/auto/16'},
          { text: "42. rapping Rain Water", link: '/auto/42'},
          { text: "167.Two Sum II - Input Array Is Sorted", link: '/auto/167'},
          { text: "680.Valid Palindrome II", link: '/auto/680'},
          // { text: "76. Minimum Window Substring", link: '/auto/76'},
          // { text: "438. Find All Anagrams in a String", link: '/auto/438'},
          // { text: "567. Permutation in String", link: '/auto/567'},
          // { text: "1422. Maximum Score After Splitting a String", link: '/auto/1422'},
          // { text: "1534. Count Good Triplets", link: '/auto/1534'},
        ]
      },
      {
        text: 'Binary Search',
        items: [
          { text: '33. Search in Rotated Sorted Array', link: '/auto/33' },
          { text: '34. Find First and Last Position of Element in Sorted Array', link: '/auto/34' },
          { text: '35. Search Insert Position', link: '/auto/35' },
          { text: '81. Search in Rotated Sorted Array II', link: '/auto/81' },
          { text: '278. First Bad Version', link: '/auto/278' },
          { text: '704. Binary Search', link: '/auto/704' },
          { text: '852. Peak Index in a Mountain Array', link: '/binary-search/852' },
          { text: '875. Koko Eating Bananas', link: '/auto/875' },
        ]
      },
      {
        text: 'Grid',
        items: [
          { text: '200. Number of Islands', link: '/grid/200' }
        ]
      },
      {
        text: 'Bitwise',
        items: [
          { text: "231.Power of Two", link: '/auto/231'},
          { text: "709.To Lower Case", link: '/auto/709'},
          { text: "1470.Shuffle the Array", link: '/auto/1470'},
        ]
      },
      {
        text: 'Hash Map',
        items: [
          { text: "30.Substring with Concatenation of All Words", link: 'auto/30'},
          { text: "49.Group Anagrams", link: 'auto/49'},
          { text: "128.Longest Consecutive Sequence", link: 'auto/128'},
          { text: "347.Top K Frequent Elements", link: 'auto/347'},
          { text: "387.First Unique Character in a String", link: 'auto/387'},
          { text: "451.Sort Characters By Frequency", link: 'auto/451'},
          { text: "895.Maximum Frequency Stack", link: 'auto/895'},
        ]
      },
      {
        text: 'Greedy Algorithm',
        items: [
          { text: "122.Best Time to Buy and Sell Stock II", link: 'auto/122'},
          { text: "134.Gas Station", link: 'auto/134'},
          { text: "*435.Non-overlapping Intervals", link: 'auto/435'},
          { text: "452.Minimum Number of Arrows to Burst Balloons", link: 'auto/452'},
          { text: "455.Assign Cookies", link: 'auto/455'},
          { text: "860.Lemonade Change", link: 'auto/860'},
        ]
      },
      {
        text: 'String && Array && Others',
        items: [
          { text: "Array", link: 'others/array/index'},
          { text: "1.Two Sum", link: '/auto/1'},
          { text: "283. Move Zeroes", link: '/auto/283'},
          { text: "509.Fibonacci Number", link: 'auto/509'},
          { text: "867.Transpose Matrix", link: '/auto/867'},
          { text: '2586.count-the-number-of-vowel-strings-in-range', link: '/others/2586' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/chrysalis1215/leetcode' }
    ]
  }
})
