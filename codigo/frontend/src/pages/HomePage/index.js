import DropFile from "../../components/DropFile";
import PageContent from "../../components/PageContent";
import Sidebar from "../../components/Sidebar";
import BlueHeader from "../../components/BlueHeader";
import PageTitle from "../../components/PageTitle";
import Container from "../../components/Container";
/**
 * HomePage Component
 * 
 * This component represents the home page of the application.
 * 
 * @returns {JSX.Element} HomePage component.
 */
export default function HomePage() {
    return (
        <Container>
            <Sidebar />
            <div>
                <BlueHeader></BlueHeader>
                <PageContent justifyContent="space-between">
                    <PageTitle>Upload de arquivos</PageTitle>
                    <DropFile />
                    <div></div>
                    {/* Div vazia para facilitar o posicionamento das outras */}
                </PageContent>
            </div>
        </Container>
    );
}
