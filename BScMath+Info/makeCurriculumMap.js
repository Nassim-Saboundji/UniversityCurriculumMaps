
fetch("./mathInfo.json") // only change this to generate a new map for another discipline
.then(response => {
       return response.json(); 
})
.then(data => {
    keys = Object.keys(data);
    //console.log(keys);

    let dataSet = [];
    for(let i = 0; i < keys.length; i++){
        //set the id inside the data object so we can trace the edges between courses
        data[keys[i]]["id"] = i;
        dataSet.push({id: data[keys[i]]["id"], label: keys[i], title: extraInfo(keys[i], data)})
    }


    let nodes = new vis.DataSet(dataSet);

    let edgeData = findEdges(keys, data);
    let edges =  new vis.DataSet(edgeData);

    let container = document.getElementById('mynetwork');

    let graphData = {
        nodes: nodes,
        edges: edges
    }

    let options = {};

    let network =  new vis.Network(container, graphData, options);
})


function findEdges(keys, data){
    let edges = [];
    for(let i = 0; i < keys.length; i++){
        let prereqsArray = data[keys[i]]["prereqs"];
        if (prereqsArray == 0 || prereqsArray.length == 0){
            continue
        } 
        for(let j = 0; j < prereqsArray.length; j++){
            if(data[prereqsArray[j]] && data[prereqsArray[j]]["id"] != data[keys[i]]["id"]){ // if the course exists and is not obsolete
                edges.push({from: data[prereqsArray[j]]["id"], to: data[keys[i]]["id"], arrows: { enabled: true, to: true }});
            }
        }
    }

    //console.log(edges);
    return edges;
}


function extraInfo(key, data){
    let description = data[key]["description"];
    descriptionAsArray = description.split(".");
    let finalInfo = "";
    for(let i = 0; i < descriptionAsArray.length; i++){
        if (i != descriptionAsArray.length - 1){
            finalInfo += descriptionAsArray[i] + ".\n"; 
        }else{
            finalInfo += descriptionAsArray[i] + "\n";
        }
    }
    if (data[key]["prereqs"] != 0){
        let stringPreReqs = data[key]["prereqs"].join(" ");
        return data[key]["name"] + "\n" + finalInfo + "Préalables ou Concomitants : \n" + stringPreReqs + "\n";
    }

    return data[key]["name"] + "\n" + finalInfo;
}