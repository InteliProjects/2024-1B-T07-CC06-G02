import React, { useCallback, useState, useEffect} from "react";
import { useNavigate } from "react-router-dom";
import { useDropzone } from "react-dropzone";
import axios from "axios";


import { Container, Dropzone, AlgorithmSelection } from "./styles";
import Button from "../Button";

const URI = "http://127.0.0.1:5000";

const algorithmRoutes = {
    "Simulated Annealing": `${URI}/submitsa`,
    "Christofides algorithm": `${URI}/submittsp`,
};

/**
 * Component for file upload with algorithm selection.
 */

export default function DropFile() {
    const navigate = useNavigate();
    const [fileNames, setFileNames] = useState([]);
    const [selectedFile, setSelectedFile] = useState(null);
    const [selectedAlgorithm, setSelectedAlgorithm] = useState("");
    /**
     * Callback called when a file is dropped in the drop area.
     * @param {Array<File>} acceptedFiles - Accepted files.
     */

    const onDrop = useCallback((acceptedFiles) => {
        setFileNames(acceptedFiles.map((file) => file.name));
        if (acceptedFiles.length > 0) {
            setSelectedFile(acceptedFiles[0]);
        }
    }, []);

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept: {
            "text/csv": [".csv"],
        },
    });

    /**
     * Event handler for changing selected algorithm.
     * @param {Event} event - Event object.
     */
    const handleAlgorithmChange = (event) => {
        setSelectedAlgorithm(event.target.value);
    };
    /**
     * Function to handle form submission.
     * Sends the selected file to the server.
     */

    useEffect(() => {
        localStorage.setItem("selectedAlgorithm", selectedAlgorithm);
    }, [selectedAlgorithm]);


    const handleSubmit = async () => {
        console.log("Handle submit called");
        if (selectedFile && selectedAlgorithm) {
            const formData = new FormData();
            formData.append("file", selectedFile);
            const route = algorithmRoutes[selectedAlgorithm];

            try {
                const result = await axios.post(route, formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                });
                console.log("Result", result);
                localStorage.setItem("taskId", result.data.task_id);
                navigate("/routes");
            } catch (error) {
                console.error("Error uploading the file", error);
            }
        } else {
            console.error("File or algorithm not selected");
        }
    };

    return (
        <Container>
            <Dropzone {...getRootProps()}>
                <input {...getInputProps()} />
                {isDragActive ? (
                    <p>Solte o seu arquivo aqui</p>
                ) : (
                    <>
                        <Button width="80%">Selecione um arquivo</Button>
                        <p>Ou arraste o seu arquivo até aqui</p>
                    </>
                )}
            </Dropzone>
            <ul>
                {fileNames.map((fileName) => (
                    <li key={fileName}>{fileName}</li>
                ))}
            </ul>
            {fileNames.length > 0 && (
                <>
                    <AlgorithmSelection>
                        <label htmlFor="algorithm">Algoritmo:</label>
                        <select
                            id="algorithm"
                            value={selectedAlgorithm}
                            onChange={handleAlgorithmChange}
                        >
                            <option value="">Selecione um algoritmo</option>
                            {Object.keys(algorithmRoutes).map((algorithm) => (
                                <option key={algorithm} value={algorithm}>
                                    {algorithm}
                                </option>
                            ))}
                        </select>
                    </AlgorithmSelection>
                    <Button width="50%" onClickFunc={handleSubmit}>
                        Enviar
                    </Button>
                </>
            )}
        </Container>
    );
}
