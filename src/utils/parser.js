import fs from 'fs';
import { join } from 'path';

class Parser {
  constructor(directory) {
    this.directory = directory;
  }

  getFiles() {
    return fs.readdirSync(this.directory).filter(file => file.endsWith('.csv'));
  }

  getFileContent(file) {
    const filePath = join(this.directory, file);
    const data = fs.readFileSync(filePath, 'utf8');
    const rows = data.split('\n').slice(1);
    return rows;
  }
}

export default Parser;