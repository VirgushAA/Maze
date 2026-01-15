
fetch("/api/maze").then(r => r.json()).then(data => drawMaze(data));
const canvas = document.getElementById('maze');

function drawMaze(data) {
    const cellSizeX = canvas.width / data.width;
    const cellSizeY = canvas.height / data.height;
    const cellSize = Math.min(cellSizeX, cellSizeY);
    // const cellSize = 10;
    ctx = document.getElementById('maze').getContext('2d');

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
    drawPath(ctx, data.path, cellSize)
}

function drawPath(ctx, path, size) {
    ctx.strokeStyle = 'red';
    ctx.lineWidth = 3;

    ctx.beginPath();
    for (let i = 0; i < path.length; i++) {
        const [x, y] = path[i];

        ctx.lineTo(
            x * size + size / 2,
            y * size + size / 2
        );
    }
    ctx.stroke()
}