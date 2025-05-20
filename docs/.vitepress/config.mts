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
        text: 'Binary Search',
        items: [
          { text: '852. Peak Index in a Mountain Array', link: '/binary-search/852' },
        ]
      },
      {
        text: 'Grid',
        items: [
          { text: '200. Number of Islands', link: '/grid/200' }
        ]
      },

      {
        text: 'String && Array && Others',
        items: [
          { text: "Array", link: 'others/array/index'},
          { text: "1.Two Sum", link: '/auto/1'},
          { text: '2586.count-the-number-of-vowel-strings-in-range', link: '/others/2586' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/chrysalis1215/leetcode' }
    ]
  }
})
