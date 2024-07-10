import Container from "../../components/Container";
import Sidebar from "../../components/Sidebar";
import BlueHeader from "../../components/BlueHeader";
import PageContent from "../../components/PageContent";
import PageTitle from "../../components/PageTitle";
import ContentSection from "../../components/ContentSection";
import Content from "../../components/Content";
import Button from "../../components/Button";
import Map from "../../components/Map"; // Importando o componente Map


import {
    DoubleSection,
    RoutesHeader,
    RoutesList,
    TableHeader,
    TableLine,
    InputFile,
    FileInput,
    Label
} from "./styles";

import { useMemo, useState, useEffect} from "react";
import axios from "axios";

const URI = "http://127.0.0.1:5000";
const algorithmRoutes = {
    "Simulated Annealing": `${URI}/submitsa`,
    "Christofides algorithm": `${URI}/submittsp`,
};

export default function RoutesPage() {
    const [routesProcessed, setRoutesProcessed] = useState(false);
    const [routes, setRoutes] = useState([]);

    const [readTime, setReadTime] = useState(0);
    const [walkSpeed, setWalkSpeed] = useState(0);
    const [maxDuration, setMaxDuration] = useState(0);
    const [selectedAlgorithm, setSelectedAlgorithm] = useState("");
    const [selectedFile, setSelectedFile] = useState(null);
    const [algSelected, setAlgSelected] = useState(() => {
        return localStorage.getItem("selectedAlgorithm")
    })


    console.log({algSelected})
    useEffect(() => {
        setTimeout(fetchFunctionStatus, 5000);
    }, []);

    useEffect(() => {
        setAlgSelected(() => {return localStorage.getItem("selectedAlgorithm")})
    }, [algSelected]);

    useEffect(() => {
        console.log("teste2" + algSelected);  
    }, [algSelected]);    

    const SAColumns = [
        { Header: "Rota", accessor: "ROTA" },
        { Header: "Sequência", accessor: "SEQUENCIA" },
        { Header: "Duração", accessor: "DURAÇÃO" },
        { Header: "Latitude", accessor: "LATITUDE" },
        { Header: "Longitude", accessor: "LONGITUDE" },
    ]

    const OtherAlgColumns =  [
        { Header: "Rota", accessor: "ROUTE" },
        { Header: "Route Code", accessor: "ROUTE_CODE" },
        { Header: "Cluster", accessor: "CLUSTER" },
        { Header: "Latitude", accessor: "LATITUDE" },
        { Header: "Longitude", accessor: "LONGITUDE" },
    ]



    function fetchFunctionStatus() {
        const taskId = localStorage.getItem("taskId");
        const url = `http://localhost:5000/status/${taskId}`;

        axios.get(url).then((response) => {
            if (response.data.status === "completed") {
                setRoutesProcessed(true);
                setRoutes(response.data.result);
            } else {
                setTimeout(fetchFunctionStatus, 5000);
            }
        });
    }

    const handleSubmit = async () => {
        console.log("Handle submit called");
        if (selectedFile && selectedAlgorithm) {
            const formData = new FormData();
            formData.append("file", selectedFile);
            let route = algorithmRoutes[selectedAlgorithm];
            route += `?read_time=${readTime}&walk_speed=${walkSpeed}&max_duration=${maxDuration}`;

            try {
                const result = await axios.post(route, formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                });
                console.log("Result", result);
                localStorage.setItem("taskId", result.data.task_id);
                //reload window
                window.location.reload();
            } catch (error) {
                console.error("Error uploading the file", error);
            }
        } else {
            console.error("File or algorithm not selected");
        }
    };

    console.log({ routes });

    return (
        <Container>
            <Sidebar />
            <div>
                <BlueHeader />
                <PageContent justifyContent="space-between">
                    <PageTitle>Rotas</PageTitle>
                    <Content>
                        <ContentSection width="100%" height="70%">
                            {routesProcessed ? (
                                <Map
                                    routes={routes.map((route) => ({
                                        latitude: route.LATITUDE,
                                        longitude: route.LONGITUDE,
                                        description: `${route.ROTA} - ${route.SEQUENCIA}`,
                                    }))}
                                />
                            ) : (
                                <h1>Processando rotas...</h1>
                            )}
                        </ContentSection>
                        <DoubleSection>
                            <ContentSection width="78%">
                                <RoutesHeader>
                                    <h1>Resultados</h1>
                                    <div>
                                        <button>Comparar algoritmos</button>
                                        <button>Exportar .csv</button>
                                    </div>
                                </RoutesHeader>
                                <RoutesList>
                                    <TableHeader>
                                        {algSelected == "Simulated Annealing" ? SAColumns.map((column, idx) => (
                                            <div key={idx}>{column.Header}</div>
                                        )): OtherAlgColumns.map((column, idx) => (
                                            <div key={idx}>{column.Header}</div>
                                        ))}
                                    </TableHeader>
                                    {routesProcessed ? (
                                        routes.map((route, idx) => (
                                            <TableLine key={idx}>
                                                {algSelected == "Simulated Annealing" ? SAColumns.map((column) => (
                                                    <div key={column.accessor}>
                                                        {route[column.accessor]}
                                                    </div>
                                                )) : OtherAlgColumns.map((column) => (
                                                    <div key={column.accessor}>
                                                        {route[column.accessor]}
                                                    </div>
                                                ))}
                                            </TableLine>
                                        ))
                                    ) : (
                                        <h1>Processando rotas...</h1>
                                    )}
                                </RoutesList>
                            </ContentSection>
                            <ContentSection width="20%">
                                <RoutesHeader>
                                    <h1>Painel de controle</h1>
                                </RoutesHeader>
                                <RoutesList>
                                    <TableHeader>
                                        <div>Filtros</div>
                                    </TableHeader>
                                    <TableLine>
                                        <InputFile>
                                            <FileInput
                                                id="file"
                                                type="file"
                                                accept=".csv"
                                                onChange={(e) => setSelectedFile(e.target.files[0])}
                                            />
                                            <Label htmlFor="file">{selectedFile ? selectedFile.name : "Carregar Arquivo"}
                                            </Label>
                                        </InputFile>
                                    </TableLine>
                                    <TableLine>
                                        <input
                                            placeholder="Velocidade de caminhada (km/h)"
                                            type="number"
                                            onChange={(e) =>
                                                setWalkSpeed(e.target.value)
                                            }
                                        />
                                    </TableLine>
                                    <TableLine>
                                        <input
                                            placeholder="Tempo de leitura (min)"
                                            type="number"
                                            onChange={(e) =>
                                                setReadTime(e.target.value)
                                            }
                                        />
                                    </TableLine>
                                    <TableLine>
                                        <input
                                            placeholder="Tempo máximo por dia (min)"
                                            type="number"
                                            onChange={(e) =>
                                                setMaxDuration(e.target.value)
                                            }
                                        />
                                    </TableLine>
                                    <TableLine>
                                        <select
                                            onChange={(e) =>
                                                setSelectedAlgorithm(
                                                    e.target.value
                                                )
                                            }
                                        >
                                            <option value="">
                                                Selecione um algoritmo
                                            </option>
                                            {Object.keys(algorithmRoutes).map(
                                                (algorithm, idx) => (
                                                    <option
                                                        key={idx}
                                                        value={algorithm}
                                                    >
                                                        {algorithm}
                                                    </option>
                                                )
                                            )}
                                        </select>
                                    </TableLine>
                                    <TableLine>
                                        <Button
                                            width="80%"
                                            height="30px"
                                            onClickFunc={() => handleSubmit()}
                                        >
                                            Aplicar
                                        </Button>
                                    </TableLine>
                                </RoutesList>
                            </ContentSection>
                        </DoubleSection>
                    </Content>
                </PageContent>
            </div>
        </Container>
    );
}
