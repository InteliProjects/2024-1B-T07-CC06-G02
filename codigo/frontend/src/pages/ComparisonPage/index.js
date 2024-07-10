import React, { useState, useEffect } from "react";
import axios from "axios";
import Container from "../../components/Container";
import Sidebar from "../../components/Sidebar";
import BlueHeader from "../../components/BlueHeader";
import PageContent from "../../components/PageContent";
import PageTitle from "../../components/PageTitle";
import Content from "../../components/Content";
import ContentSection from "../../components/ContentSection";
import Button from "../../components/Button";
import { StyledSelect, ComparisonSection } from "./styles";
import styled from "styled-components";
import {
    TableHeader,
    TableLine,
    RoutesList,
    RoutesHeader,
    InputFile,
    FileInput,
    Label,
} from "../RoutesPage/styles";

const URI = "http://127.0.0.1:5000";

const algorithmRoutes = {
    "Simulated Annealing": `${URI}/submitsa`,
    "Christofides algorithm": `${URI}/submittsp`,
};

export default function ComparisonPage() {
    const [selectedAlgorithm1, setSelectedAlgorithm1] = useState(
        "Simulated Annealing"
    );
    const [selectedAlgorithm2, setSelectedAlgorithm2] = useState(
        "Christofides Algorithm"
    );
    const [selectedFile1, setSelectedFile1] = useState(null);
    const [selectedFile2, setSelectedFile2] = useState(null);

    const [results1, setResults1] = useState(null);
    const [results2, setResults2] = useState(null);

    const handleSubmit = async (buttonClicked) => {
        console.log("Handle submit called");
        if (
            (selectedFile1 && selectedAlgorithm1) ||
            (selectedFile2 && selectedAlgorithm2)
        ) {
            const formData = new FormData();
            const selectedFile =
                buttonClicked === 1 ? selectedFile1 : selectedFile2;
            const selectedAlgorithm =
                buttonClicked === 1 ? selectedAlgorithm1 : selectedAlgorithm2;

            formData.append("file", selectedFile);
            const route = algorithmRoutes[selectedAlgorithm];

            try {
                const result = await axios.post(route, formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                });
                console.log("Result", result);
                localStorage.setItem(
                    "taskId" + buttonClicked,
                    result.data.task_id
                );

                fetchFunctionStatus(buttonClicked);
            } catch (error) {
                console.error("Error uploading the file", error);
            }
        } else {
            console.error("File or algorithm not selected");
        }
    };

    function fetchFunctionStatus(buttonClicked) {
        const taskId = localStorage.getItem("taskId" + buttonClicked);
        const url = `http://localhost:5000/status/${taskId}`;

        axios.get(url).then((response) => {
            if (response.data.status === "completed") {
                if (buttonClicked === 1) {
                    setResults1({ ...response.data.result });
                } else {
                    setResults2({ ...response.data.result });
                }
            } else {
                setTimeout(() => fetchFunctionStatus(buttonClicked), 5000);
            }
        });
    }

    return (
        <Container>
            <Sidebar />
            <div>
                <BlueHeader />
                <PageContent justifyContent="space-between">
                    <PageTitle>Comparação de algoritmos</PageTitle>
                    <Content flexDirection="row" justifyContent="space-evenly">
                        <ContentSection width="40%" height="80%">
                            <input
                                type="file"
                                accept=".csv"
                                onChange={(e) =>
                                    setSelectedFile1(e.target.files[0])
                                }
                            />
                            <StyledSelect>
                                <select
                                    value={selectedAlgorithm1}
                                    onChange={(e) =>
                                        setSelectedAlgorithm1(e.target.value)
                                    }
                                >
                                    <option value="Simulated Annealing">
                                        Simulated Annealing
                                    </option>
                                    <option value="Christofides algorithm">
                                        Christofides algorithm
                                    </option>
                                </select>
                            </StyledSelect>
                            <ComparisonSection>
                                {results1 ? (
                                    <>
                                        <div>
                                            Número de dias:
                                            {results1[0].TOTAL_DAYS}
                                        </div>
                                        <div>
                                            Distância total (km):
                                            {results1[0].TOTAL_DISTANCE?.toFixed(
                                                2
                                            )}
                                        </div>
                                        <div>
                                            Número de leituristas:{" "}
                                            {results1[0].NUM_READERS}
                                        </div>
                                    </>
                                ) : (
                                    <div>Loading data...</div>
                                )}
                            </ComparisonSection>
                            <button onClick={() => handleSubmit(1)}>
                                Rodar
                            </button>
                        </ContentSection>

                        <ContentSection width="40%" height="80%">
                            <input
                                type="file"
                                accept=".csv"
                                onChange={(e) =>
                                    setSelectedFile2(e.target.files[0])
                                }
                            />
                            <StyledSelect>
                                <select
                                    value={selectedAlgorithm2}
                                    onChange={(e) =>
                                        setSelectedAlgorithm2(e.target.value)
                                    }
                                >
                                    <option value="Simulated Annealing">
                                        Simulated Annealing
                                    </option>
                                    <option value="Christofides algorithm">
                                        Christofides algorithm
                                    </option>
                                </select>
                            </StyledSelect>

                            <ComparisonSection>
                                {results2 ? (
                                    <>
                                        <div>
                                            Número de dias:
                                            {results2[0].TOTAL_DAYS}
                                        </div>
                                        <div>
                                            Distância total (km):
                                            {results2[0].TOTAL_DISTANCE?.toFixed(
                                                2
                                            )}
                                        </div>
                                        <div>
                                            Número de leituristas:{" "}
                                            {results2[0].NUM_READERS}
                                        </div>
                                    </>
                                ) : (
                                    <div>Loading data...</div>
                                )}
                            </ComparisonSection>
                            <button onClick={() => handleSubmit(2)}>
                                Rodar
                            </button>
                        </ContentSection>
                    </Content>
                </PageContent>
            </div>
        </Container>
    );
}
