#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const inputStr = process.argv[2]; // Grab input from CLI

if (!inputStr) {
  console.error("❌ Please provide input like: '[11]Two Sum'");
  process.exit(1);
}

const outputDir = path.join(__dirname, '../docs/auto')

const templatePath = path.join(__dirname, 'generate.md');
function loadTemplate(templatePath) {
  return fs.readFileSync(templatePath, 'utf8');
}

function renderTemplate(template, data) {
  return template
    .replace(/{{id}}/g, data.id)
    .replace(/{{name}}/g, data.name);
}

function generateMarkdown() {

  const match = inputStr.match(/^\[(\d+)\](.+)$/);
  if (!match) {
    throw new Error("Invalid input format. Use format like '[11]Two Sum'");
  }

  const problemId = match[1];
  const problemName = match[2].trim();
  const fileName = `${problemId}.md`;

  // Load template and inject values
  const template = loadTemplate(templatePath);
  const content = renderTemplate(template, { id: problemId, name: problemName });

  // Ensure output folder exists
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const filePath = path.join(outputDir, fileName);
  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Markdown file "${fileName}" created successfully.`);
  console.log(`You could add new route link to vitepress's config.mts`);
  console.log(`{ text: "${problemId}.${problemName}", link: 'auto/${problemId}'},`);

}

generateMarkdown();