import { useNavigate } from "react-router-dom";

import { Container, LogoHolder, PageSelection, PageButton } from "./styles";
import logo from "../../assets/logo-onda.png";

export default function Sidebar() {
    const navigate = useNavigate();

    return (
        <Container>
            <LogoHolder>
                <img src={logo} alt="Logo" />
                <h1>Painel de controle</h1>
            </LogoHolder>
            <PageSelection>
                <PageButton onClick={() => navigate("/home")}>
                    Upload de arquivos
                </PageButton>
                <PageButton onClick={() => navigate("/routes")}>
                    Rotas
                </PageButton>
                <PageButton onClick={() => navigate("/comparison")}>
                    Algoritmos
                </PageButton>
            </PageSelection>
        </Container>
    );
}
