<p>You are given a string <code>s</code> and an array of strings <code>words</code>. All the strings of <code>words</code> are of <strong>the same length</strong>.</p>

<p>A <strong>concatenated string</strong> is a string that exactly contains all the strings of any permutation of <code>words</code> concatenated.</p>

<ul> 
 <li>For example, if <code>words = ["ab","cd","ef"]</code>, then <code>"abcdef"</code>, <code>"abefcd"</code>, <code>"cdabef"</code>, <code>"cdefab"</code>, <code>"efabcd"</code>, and <code>"efcdab"</code> are all concatenated strings. <code>"acdbef"</code> is not a concatenated string because it is not the concatenation of any permutation of <code>words</code>.</li> 
</ul>

<p>Return an array of <em>the starting indices</em> of all the concatenated substrings in <code>s</code>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<div class="example-block"> 
 <p><strong>Input:</strong> <span class="example-io">s = "barfoothefoobarman", words = ["foo","bar"]</span></p> 
</div>

<p><strong>Output:</strong> <span class="example-io">[0,9]</span></p>

<p><strong>Explanation:</strong></p>

<p>The substring starting at 0 is <code>"barfoo"</code>. It is the concatenation of <code>["bar","foo"]</code> which is a permutation of <code>words</code>.<br /> The substring starting at 9 is <code>"foobar"</code>. It is the concatenation of <code>["foo","bar"]</code> which is a permutation of <code>words</code>.</p>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block"> 
 <p><strong>Input:</strong> <span class="example-io">s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]</span></p> 
</div>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no concatenated substring.</p>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block"> 
 <p><strong>Input:</strong> <span class="example-io">s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]</span></p> 
</div>

<p><strong>Output:</strong> <span class="example-io">[6,9,12]</span></p>

<p><strong>Explanation:</strong></p>

<p>The substring starting at 6 is <code>"foobarthe"</code>. It is the concatenation of <code>["foo","bar","the"]</code>.<br /> The substring starting at 9 is <code>"barthefoo"</code>. It is the concatenation of <code>["bar","the","foo"]</code>.<br /> The substring starting at 12 is <code>"thefoobar"</code>. It is the concatenation of <code>["the","foo","bar"]</code>.</p>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li> 
 <li><code>1 &lt;= words.length &lt;= 5000</code></li> 
 <li><code>1 &lt;= words[i].length &lt;= 30</code></li> 
 <li><code>s</code> and <code>words[i]</code> consist of lowercase English letters.</li> 
</ul>

<div><div>Related Topics</div><div><li>哈希表</li><li>字符串</li><li>滑动窗口</li></div></div><br><div><li>👍 1233</li><li>👎 0</li></div>