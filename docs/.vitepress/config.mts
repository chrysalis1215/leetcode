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
        text: 'Hashing',
        items: [
          { text: "128.Longest Consecutive Sequence", link: 'auto/128'},
          // { text: "1.Two Sum", link: '/auto/1'},
          // { text: "283. Move Zeroes", link: '/auto/283'},
          // { text: "867.Transpose Matrix", link: '/auto/867'},
          // { text: '2586.count-the-number-of-vowel-strings-in-range', link: '/others/2586' }
        ]
      },
      {
        text: 'String && Array && Others',
        items: [
          { text: "Array", link: 'others/array/index'},
          { text: "1.Two Sum", link: '/auto/1'},
          { text: "283. Move Zeroes", link: '/auto/283'},
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
