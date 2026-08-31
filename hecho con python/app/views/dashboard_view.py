from fastapi.responses import HTMLResponse

def get_dashboard_html() -> str:
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NOTASYA - Dashboard Académico</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-slate-50 font-sans text-slate-800">
    <!-- Header -->
    <header class="bg-gradient-to-r from-emerald-800 to-teal-700 text-white shadow-lg">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="p-2 bg-white/10 rounded-lg backdrop-blur">
                    <i class="fa-solid fa-graduation-cap text-2xl text-emerald-300"></i>
                </div>
                <div>
                    <h1 class="text-2xl font-bold tracking-tight">NOTASYA</h1>
                    <p class="text-xs text-emerald-200">Universidad de Manizales · Facultad de Ciencias e Ingeniería</p>
                </div>
            </div>
            <div class="flex items-center space-x-3">
                <a href="/docs" target="_blank" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-sm font-semibold shadow transition flex items-center gap-2">
                    <i class="fa-solid fa-book"></i> Swagger Docs
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <!-- KPI Cards -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-center justify-between">
                <div>
                    <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Estudiantes</p>
                    <p id="kpi-estudiantes" class="text-3xl font-extrabold text-slate-900 mt-1">...</p>
                </div>
                <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center text-xl">
                    <i class="fa-solid fa-user-graduate"></i>
                </div>
            </div>

            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-center justify-between">
                <div>
                    <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Profesores</p>
                    <p id="kpi-profesores" class="text-3xl font-extrabold text-slate-900 mt-1">...</p>
                </div>
                <div class="w-12 h-12 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center text-xl">
                    <i class="fa-solid fa-chalkboard-user"></i>
                </div>
            </div>

            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-center justify-between">
                <div>
                    <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Cursos Activos</p>
                    <p id="kpi-cursos" class="text-3xl font-extrabold text-slate-900 mt-1">...</p>
                </div>
                <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-xl">
                    <i class="fa-solid fa-book-bookmark"></i>
                </div>
            </div>

            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-center justify-between">
                <div>
                    <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Promedio General</p>
                    <p id="kpi-promedio" class="text-3xl font-extrabold text-emerald-600 mt-1">...</p>
                </div>
                <div class="w-12 h-12 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center text-xl">
                    <i class="fa-solid fa-star"></i>
                </div>
            </div>
        </div>

        <!-- Charts & Actions Section -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
            <!-- Chart 1 -->
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 lg:col-span-2">
                <h3 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-chart-column text-emerald-600"></i> Distribución de Calificaciones por Curso
                </h3>
                <div class="h-64">
                    <canvas id="gradesChart"></canvas>
                </div>
            </div>

            <!-- Quick Registration Box -->
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
                <h3 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-plus-circle text-emerald-600"></i> Registro Rápido Estudiante
                </h3>
                <form id="form-estudiante" class="space-y-4" onsubmit="crearEstudiante(event)">
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 mb-1">Nombre Completo</label>
                        <input type="text" id="est-nombre" required class="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-emerald-500 outline-none" placeholder="Ej: Camilo Pérez">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 mb-1">Teléfono</label>
                        <input type="text" id="est-telefono" required class="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-emerald-500 outline-none" placeholder="Ej: 3105554433">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 mb-1">Correo Institucional</label>
                        <input type="email" id="est-correo" required class="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-emerald-500 outline-none" placeholder="cperez@umanizales.edu.co">
                    </div>
                    <button type="submit" class="w-full py-2.5 bg-emerald-700 hover:bg-emerald-600 text-white rounded-lg text-sm font-semibold shadow transition">
                        Registrar Estudiante
                    </button>
                </form>
                <div id="form-feedback" class="mt-3 text-xs hidden p-3 rounded-lg"></div>
            </div>
        </div>

        <!-- Tables Section -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- Estudiantes List -->
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
                <h3 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-users text-blue-600"></i> Estudiantes Matriculados
                </h3>
                <div class="overflow-x-auto max-h-72">
                    <table class="w-full text-left text-sm text-slate-600">
                        <thead class="bg-slate-50 text-slate-700 uppercase text-xs font-semibold sticky top-0">
                            <tr>
                                <th class="px-4 py-3">ID</th>
                                <th class="px-4 py-3">Nombre</th>
                                <th class="px-4 py-3">Correo</th>
                            </tr>
                        </thead>
                        <tbody id="tabla-estudiantes" class="divide-y divide-slate-100">
                            <tr><td colspan="3" class="text-center py-4 text-slate-400">Cargando datos...</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Cursos List -->
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
                <h3 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-award text-amber-500"></i> Calificaciones de Cursos
                </h3>
                <div class="overflow-x-auto max-h-72">
                    <table class="w-full text-left text-sm text-slate-600">
                        <thead class="bg-slate-50 text-slate-700 uppercase text-xs font-semibold sticky top-0">
                            <tr>
                                <th class="px-4 py-3">Asignatura</th>
                                <th class="px-4 py-3">Estudiante</th>
                                <th class="px-4 py-3">Nota</th>
                                <th class="px-4 py-3">Estado</th>
                            </tr>
                        </thead>
                        <tbody id="tabla-cursos" class="divide-y divide-slate-100">
                            <tr><td colspan="4" class="text-center py-4 text-slate-400">Cargando datos...</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </main>

    <footer class="text-center py-6 text-xs text-slate-400 border-t mt-8">
        NOTASYA &copy; 2026 - Taller de Diseño de Sistemas de Información · Hildebrando Tangarife Cardona
    </footer>

    <script>
        let chartInstance = null;

        async function loadData() {
            try {
                // KPIs
                const resStats = await fetch('/api/v1/analitica/resumen');
                const stats = await resStats.json();
                document.getElementById('kpi-estudiantes').innerText = stats.total_estudiantes;
                document.getElementById('kpi-profesores').innerText = stats.total_profesores;
                document.getElementById('kpi-cursos').innerText = stats.total_cursos;
                document.getElementById('kpi-promedio').innerText = stats.promedio_general.toFixed(1);

                // Estudiantes
                const resEst = await fetch('/api/v1/estudiantes');
                const estudiantes = await resEst.json();
                const tbodyEst = document.getElementById('tabla-estudiantes');
                tbodyEst.innerHTML = estudiantes.map(e => `
                    <tr class="hover:bg-slate-50 transition">
                        <td class="px-4 py-2.5 font-bold text-slate-800">#${e.id}</td>
                        <td class="px-4 py-2.5 font-medium">${e.nombre}</td>
                        <td class="px-4 py-2.5 text-slate-500">${e.correo}</td>
                    </tr>
                `).join('') || '<tr><td colspan="3" class="text-center py-4">No hay estudiantes</td></tr>';

                // Cursos
                const resCursos = await fetch('/api/v1/cursos');
                const cursos = await resCursos.json();
                const tbodyCursos = document.getElementById('tabla-cursos');
                tbodyCursos.innerHTML = cursos.map(c => {
                    const badgeClass = c.calificacion >= 4.5 
                        ? 'bg-amber-100 text-amber-800' 
                        : (c.calificacion >= 3.0 ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800');
                    const badgeText = c.calificacion >= 4.5 ? 'Honor' : (c.calificacion >= 3.0 ? 'Aprobado' : 'Reprobado');
                    return `
                        <tr class="hover:bg-slate-50 transition">
                            <td class="px-4 py-2.5 font-medium text-slate-800">${c.nombre}</td>
                            <td class="px-4 py-2.5">${c.estudiante ? c.estudiante.nombre : 'ID: ' + c.estudiante_id}</td>
                            <td class="px-4 py-2.5 font-bold">${c.calificacion.toFixed(1)}</td>
                            <td class="px-4 py-2.5"><span class="px-2 py-0.5 rounded-full text-xs font-semibold ${badgeClass}">${badgeText}</span></td>
                        </tr>
                    `;
                }).join('') || '<tr><td colspan="4" class="text-center py-4">No hay cursos registrados</td></tr>';

                // Render Chart
                renderChart(cursos);
            } catch (err) {
                console.error(err);
            }
        }

        function renderChart(cursos) {
            const ctx = document.getElementById('gradesChart').getContext('2d');
            const labels = cursos.map(c => c.nombre.length > 15 ? c.nombre.substring(0, 15) + '...' : c.nombre);
            const data = cursos.map(c => c.calificacion);

            if (chartInstance) chartInstance.destroy();

            chartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels.length ? labels : ['Sin datos'],
                    datasets: [{
                        label: 'Calificación (0 - 5.0)',
                        data: data.length ? data : [0],
                        backgroundColor: data.map(n => n >= 3.0 ? 'rgba(16, 185, 129, 0.7)' : 'rgba(239, 68, 68, 0.7)'),
                        borderColor: data.map(n => n >= 3.0 ? 'rgb(16, 185, 129)' : 'rgb(239, 68, 68)'),
                        borderWidth: 1,
                        borderRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: { min: 0, max: 5.0, ticks: { stepSize: 1.0 } }
                    }
                }
            });
        }

        async function crearEstudiante(e) {
            e.preventDefault();
            const feedback = document.getElementById('form-feedback');
            feedback.className = "mt-3 text-xs p-3 rounded-lg";
            feedback.classList.remove('hidden');

            const payload = {
                nombre: document.getElementById('est-nombre').value,
                telefono: document.getElementById('est-telefono').value,
                correo: document.getElementById('est-correo').value
            };

            try {
                const res = await fetch('/api/v1/estudiantes', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const data = await res.json();
                if (res.ok) {
                    feedback.className = "mt-3 text-xs p-3 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
                    feedback.innerText = "¡Estudiante registrado exitosamente!";
                    document.getElementById('form-estudiante').reset();
                    loadData();
                } else {
                    feedback.className = "mt-3 text-xs p-3 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
                    feedback.innerText = "Error: " + (data.detail || "No se pudo registrar.");
                }
            } catch (err) {
                feedback.className = "mt-3 text-xs p-3 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
                feedback.innerText = "Error de conexión con el servidor.";
            }
        }

        window.onload = loadData;
    </script>
</body>
</html>
"""
