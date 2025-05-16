import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
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
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/chrysalis1215/leetcode' }
    ]
  }
})
