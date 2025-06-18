const API_URL = '/productos';

document.addEventListener('DOMContentLoaded', () => {
  cargarProductos();

  document.getElementById('formCrear').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
      codigo: document.getElementById('crearCodigo').value,
      nombre: document.getElementById('crearNombre').value,
      precio: parseFloat(document.getElementById('crearPrecio').value),
      foto: document.getElementById('crearFoto').value,
      categoria: document.getElementById('crearCategoria').value
    };
    await fetch(API_URL + '/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    e.target.reset();
    document.querySelector('[data-modal-hide="crearModal"]').click();
    cargarProductos();
  });

  document.getElementById('formEditar').addEventListener('submit', async (e) => {
    e.preventDefault();
    const codigo = document.getElementById('editarCodigo').value;
    const data = {
      nombre: document.getElementById('editarNombre').value,
      precio: parseFloat(document.getElementById('editarPrecio').value),
      foto: document.getElementById('editarFoto').value,
      categoria: document.getElementById('editarCategoria').value
    };
    await fetch(`${API_URL}/${codigo}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    document.querySelector('[data-modal-hide="editarModal"]').click();
    cargarProductos();
  });
});

async function cargarProductos() {
  const res = await fetch(API_URL + '/');
  const productos = await res.json();
  const tbody = document.getElementById('productosTabla');
  tbody.innerHTML = '';
  productos.forEach(p => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td class="px-3 py-2">${p.codigo}</td>
      <td class="px-3 py-2">${p.nombre}</td>
      <td class="px-3 py-2">$${p.precio.toFixed(2)}</td>
      <td class="px-3 py-2"><img src="${p.foto}" alt="" width="50"></td>
      <td class="px-3 py-2">${p.categoria}</td>
      <td class="px-3 py-2 text-center">
        <button onclick="abrirEditar('${p.codigo}')" class="text-yellow-600 hover:underline mr-2">Editar</button>
        <button onclick="eliminar('${p.codigo}')" class="text-red-600 hover:underline">Eliminar</button>
      </td>`;
    tbody.appendChild(row);
  });
}

async function eliminar(codigo) {
  await fetch(`${API_URL}/${codigo}`, { method: 'DELETE' });
  cargarProductos();
}

async function abrirEditar(codigo) {
  const res = await fetch(`${API_URL}/${codigo}`);
  const p = await res.json();

  document.getElementById('editarCodigo').value = p.codigo;
  document.getElementById('editarNombre').value = p.nombre;
  document.getElementById('editarPrecio').value = p.precio;
  document.getElementById('editarFoto').value = p.foto;
  document.getElementById('editarCategoria').value = p.categoria;
  const modalEditarEl = document.getElementById('editarModal');
  const modalEditar = new Modal(modalEditarEl);
  modalEditar.show();
}

