async function uploadFile(){
            let file=document.getElementById("fileInput").files[0];
            let w=document.getElementById("weight").value;
            let b=document.getElementById("bias").value;
            let alpha=document.getElementById("alpha").value;
            let i=document.getElementById("iterations").value;

            let w_f=document.getElementById("wFinal");
            let b_f=document.getElementById("bFinal");
            let cost_f=document.getElementById("costFinal");
            let r2=document.getElementById("r2");
            const formData=new FormData();
            formData.append("file",file);
            formData.append("weight",w);
            formData.append("bias",b);
            formData.append("alpha",alpha);
            formData.append("iterations",i);

            const response=await fetch("/upload",{method:"POST",body:formData});
            const data = await response.json();

            const bust=new Date();

            document.getElementById("regression").src = "/plots/"+ data.regression_plot+"?"+bust;
            document.getElementById("cost").src = "/plots/"+data.cost_plot+"?"+bust;
            w_f.innerText="Final weight: "+data.w;
            b_f.innerText="Final bias: "+data.b;
            cost_f.innerText="Final cost: "+data.cost;
            r2.innerHTML="Final R² value: "+data.r2;

            const table = document.getElementById("datasetPreview");
            table.innerHTML = "";
            let headerRow = "<tr>";

            data.columns.forEach(col => {
                headerRow += `<th>${col}</th>`;
            });
            headerRow += "</tr>";
            table.innerHTML += headerRow;

            data.preview.forEach(row => {
            let rowHTML = "<tr>";
            data.columns.forEach(col => {
                rowHTML += `<td>${row[col]}</td>`;
            });
            rowHTML += "</tr>";
            table.innerHTML += rowHTML;});

            

            let history = document.getElementById("history");

            let row = `
            <tr>
            <td>${alpha}</td>
            <td>${i}</td>
            <td>${w}</td>
            <td>${b}</td>
            <td>${data.w.toFixed(4)}</td>
            <td>${data.b.toFixed(4)}</td>
            <td>${data.cost.toFixed(4)}</td>
            <td>${data.r2.toFixed(4)}</td>
            </tr>
            `;

            history.innerHTML += row;

        



        }