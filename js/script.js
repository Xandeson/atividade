let cont = 0;

        function addItem() {
            const input = document.getElementById('itemInput');
            const itemText = input.value.trim();

            if (itemText === '') {
                alert('Por favor, digite um item!');
                return;
            }

            cont++;
            const itemList = document.getElementById('item');
            const novoItem = document.createElement('li');
            novoItem.textContent = `${cont}. ${itemText}`;
            itemList.appendChild(novoItem);

            input.value = ''; 
            input.focus(); 
        }

        document.getElementById('addButton').addEventListener('click', addItem);

        // Permite adicionar item ao pressionar 'Enter'
        document.getElementById('itemInput').addEventListener('keypress', function (event) {
            if (event.key === 'Enter') {
                addItem();
            }
        });