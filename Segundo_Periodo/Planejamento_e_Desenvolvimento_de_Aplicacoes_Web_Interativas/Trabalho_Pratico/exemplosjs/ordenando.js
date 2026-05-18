const swap = (vetor, pos1, pos2) => {
    let temp = vetor[pos1];
    vetor[pos1] = vetor[pos2];
    vetor[pos2] = temp;
};

const shuffle = (vetor, qtd_trocas) => {
    for (let i = 0; i < qtd_trocas; i++) {
        let pos1 = Math.floor(Math.random() * vetor.length);
        let pos2 = Math.floor(Math.random() * vetor.length);
        swap(vetor, pos1, pos2);
    }
};

const bubble_sort = (vetor) => {
    let n = vetor.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                swap(vetor, j, j + 1);
            }
        }
    }
    return vetor;
};

const selection_sort = (vetor) => {
    let n = vetor.length;
    for (let i = 0; i < n - 1; i++) {
        let min_idx = i;
        for (let j = i + 1; j < n; j++) {
            if (vetor[j] < vetor[min_idx]) {
                min_idx = j;
            }
        }
        swap(vetor, min_idx, i);
    }
    return vetor;
};

const particionamento = (vetor, pos_inicial, pos_final, pivot) => {
    let i = pos_inicial;
    let j = pos_final;
    while (i <= j) {
        while (vetor[i] < pivot) {
            i++;
        }
        while (vetor[j] > pivot) {
            j--;
        }
        if (i <= j) {
            swap(vetor, i, j);
            i++;
            j--;
        }
    }
    return i;
};

const quick_sort = (vetor, pos_inicial, pos_final) => {
    if (pos_inicial < pos_final) {
        let pivot = vetor[Math.floor((pos_inicial + pos_final) / 2)];
        let pi = particionamento(vetor, pos_inicial, pos_final, pivot);
        quick_sort(vetor, pos_inicial, pi - 1);
        quick_sort(vetor, pi, pos_final);
    }
    return vetor;
};
