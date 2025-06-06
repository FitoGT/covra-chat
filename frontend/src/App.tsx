import { useState, useRef, useEffect } from 'react'
import { useGenerateCoverLetterMutation } from './client/mutations/useCoverLettersMutations'
import covraIcon from './assets/covra-icon.png'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

function App() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [error, setError] = useState('')
  const [step, setStep] = useState<'cv' | 'job' | 'chat'>('cv')
  const [cv, setCv] = useState<string>('')
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const { mutateAsync, isPending } = useGenerateCoverLetterMutation()

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim()) return

    const userMessage = input.trim()
    setInput('')
    setError('')

    if (step === 'cv') {
      setCv(userMessage)
      setMessages([{ role: 'user', content: `CV: ${userMessage}` }])
      setStep('job')
      return
    }

    if (step === 'job') {
      setMessages(prev => [...prev, { role: 'user', content: `Job Description: ${userMessage}` }])
      setStep('chat')
      await handleCoverLetterGeneration(userMessage)
      return
    }

    setMessages(prev => [...prev, { role: 'user', content: userMessage }])
  }

  const handleCoverLetterGeneration = async (jobDescription: string) => {
  setError('')

  try {
    const response = await mutateAsync({
      cv,
      job_description: jobDescription,
    })

    setMessages(prev => [...prev, { role: 'assistant', content: response.cover_letter }])
  } catch (err) {
    console.error('Error generating cover letter:', err)
    setError('Failed to generate cover letter. Please check your API key and try again.')
  }
}

  const handleNewCoverLetter = () => {
    setMessages([{ role: 'user', content: `CV: ${cv}` }])
    setStep('job')
  }

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      <header className="bg-white shadow-sm py-4 px-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <img src={covraIcon} alt="Covra Icon" className="h-8 w-8" />
            <h1 className="text-xl font-semibold text-gray-800">Cover Letter Generator</h1>
          </div>
          {step === 'chat' && (
            <button
              onClick={handleNewCoverLetter}
              className="px-4 py-2 bg-indigo-600 text-white font-medium rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              New Cover Letter
            </button>
          )}
        </div>
      </header>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full text-gray-500">
            <p className="text-lg mb-2">Welcome to Covra Chat, your AI assistant for Cover Letters</p>
            <p>Please paste your CV to get started</p>
          </div>
        ) : (
          messages.map((message, index) => (
            <div
              key={index}
              className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              <div
                className={`max-w-[80%] rounded-lg p-4 ${
                  message.role === 'user'
                    ? 'bg-indigo-600 text-white'
                    : 'bg-white text-gray-800 shadow'
                }`}
              >
                <p className="whitespace-pre-line">{message.content}</p>
              </div>
            </div>
          ))
        )}
        {isPending && (
          <div className="flex justify-start">
            <div className="bg-white text-gray-800 rounded-lg p-4 shadow">
              <div className="flex space-x-2">
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></div>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {error && (
        <div className="bg-red-50 border-l-4 border-red-400 p-4 mx-4 mb-4">
          <p className="text-red-700">{error}</p>
        </div>
      )}

      <form onSubmit={handleSubmit} className="border-t border-gray-200 p-4 bg-white">
        <div className="flex space-x-4">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder={
              step === 'cv'
                ? 'Paste your CV here...'
                : step === 'job'
                ? 'Paste the job description here...'
                : 'Type your message...'
            }
            className="flex-1 p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
            disabled={isPending}
          />
          <button
            type="submit"
            className="px-4 py-2 bg-indigo-600 text-white font-medium rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
            disabled={isPending || !input.trim()}
          >
            Send
          </button>
        </div>
      </form>
    </div>
  )
}

export default App
