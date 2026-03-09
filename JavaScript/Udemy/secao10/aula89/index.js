const fs = require("fs").promises
const path = require("path")

async function readdir(root_dir) {
    root_dir = root_dir || path.resolve(__dirname)
    const files = await fs.readdir(root_dir)

    walk(files, root_dir)
}

async function walk(files, root_dir) {
    for(let file of files) {
        const file_full_path = path.resolve(root_dir, file)
        const stats = await fs.stat(file_full_path)
        
        if (/\.git/g.test(file_full_path)) continue
        if (/node_modules/g.test(file_full_path)) continue
        
        if (stats.isDirectory()) {
            readdir(file_full_path)
            continue
        }
        
        if (!/\.css$/g.test(file_full_path)) continue

        console.log(file_full_path)
    }
}

readdir("/home/samuel/GitHub/Estudos/JavaScript/Udemy")