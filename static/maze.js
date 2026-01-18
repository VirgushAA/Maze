document.getElementById('build-form').addEventListener('submit', async (e) => { e.preventDefault(); });
document.getElementById('solve-form').addEventListener('submit', async (e) => { e.preventDefault(); });

const canvas = document.getElementById('maze');

let cellSizeX = null;
let cellSizeY = null;
let cellSize = null;

let maze = null;
let path = null;

document.getElementById("button_build").addEventListener('click', async () => {
    const form = document.getElementById('build-form');
    const formData = new FormData(form);

    payload = {
        width: Number(formData.get('width')) || 20,
        height: Number(formData.get('height')) || 20,
        algorithm: formData.get('build-algorithm')
    };

    const response = await fetch('/api/maze/build', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    });

    maze = await response.json();
    drawMaze(maze);
});


document.getElementById('button_solve').addEventListener('click', async () => {
    if (!maze) return alert('No maze to solve.');

    const form = document.getElementById('solve-form');
    const formData = new FormData(form);

    payload = {
        maze: maze,
        algorithm: formData.get('solve-algorithm'),
        start: [0, 0],
        finish: [maze.width - 1, maze.height - 1],
    };

    const response = await fetch('/api/maze/solve', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    });

    path = await response.json();
    drawPath(path);
});

function drawMaze(data) {

    cellSizeX = canvas.width / data.width;
    cellSizeY = canvas.height / data.height;
    cellSize = Math.min(cellSizeX, cellSizeY);
    
    ctx = canvas.getContext('2d');
    
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.translate(0.5, 0.5);

    ctx.lineWidth = 2;
    ctx.strokeStyle = 'black';
    for(let y = 0; y < data.height; y++) {
        for(let x = 0; x < data.width; x++) {
            
            const px = x * cellSize;
            const py = y * cellSize;

            if (data.verticals[y][x] === 1) {
                ctx.beginPath();
                ctx.moveTo(px + cellSize, py);
                ctx.lineTo(px + cellSize, py + cellSize);
                ctx.stroke();
            }
            if (data.horizontals[y][x] === 1) {
                ctx.beginPath();
                ctx.moveTo(px, py + cellSize);
                ctx.lineTo(px + cellSize, py + cellSize);
                ctx.stroke();
            }
        }
    }
}

function drawPath(path) {
    ctx = canvas.getContext('2d');

    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.translate(0.5, 0.5);

    ctx.strokeStyle = 'red';
    ctx.lineWidth = 3;

    ctx.beginPath();
    ctx.moveTo(
        path[0][0] * cellSize + cellSize / 2,
        path[0][1] * cellSize + cellSize / 2
    );
    for (let i = 0; i < path.length; i++) {
        const [x, y] = path[i];

        ctx.lineTo(
            x * cellSize + cellSize / 2,
            y * cellSize + cellSize / 2
        );
    }
    ctx.stroke();
}
